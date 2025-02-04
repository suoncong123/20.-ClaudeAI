from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
import re

class CodeService:
    def __init__(self):
        self.code_pattern = re.compile(r'```(\w+)?\n(.*?)\n```', re.DOTALL)
        self.formatter = HtmlFormatter(style='monokai', 
                                    cssclass='highlight',
                                    linenos=True)

    def process_code_blocks(self, content):
        """Xử lý và highlight code trong nội dung"""
        has_code = False
        position = 0
        result = []

        for match in self.code_pattern.finditer(content):
            # Thêm text trước code block
            result.append(content[position:match.start()])
            
            # Xử lý code block
            language = match.group(1) or 'text'
            code = match.group(2)
            
            try:
                lexer = get_lexer_by_name(language)
            except ValueError:
                try:
                    lexer = guess_lexer(code)
                except ValueError:
                    lexer = get_lexer_by_name('text')

            highlighted_code = highlight(code, lexer, self.formatter)
            result.append(f'<div class="code-block" data-language="{language}">')
            result.append('<div class="code-header">')
            result.append(f'<span class="code-language">{language}</span>')
            result.append('<button class="copy-button">Copy</button>')
            result.append('</div>')
            result.append(highlighted_code)
            result.append('</div>')

            position = match.end()
            has_code = True

        # Thêm text còn lại
        result.append(content[position:])

        return ''.join(result), has_code

    def get_css(self):
        """Lấy CSS cho code highlighting"""
        return self.formatter.get_style_defs('.highlight')