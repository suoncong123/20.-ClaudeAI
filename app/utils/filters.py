from flask import Blueprint
from markupsafe import escape, Markup
from jinja2 import pass_eval_context

blueprint = Blueprint('filters', __name__)

@blueprint.app_template_filter('nl2br')
@pass_eval_context
def nl2br(eval_ctx, value):
    """Convert newlines to <br> tags"""
    if not value:
        return ''
    
    value = escape(value)
    result = value.replace('\n', Markup('<br>\n'))
    
    if eval_ctx.autoescape:
        result = Markup(result)
        
    return result