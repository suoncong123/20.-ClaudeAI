import os
from anthropic import Anthropic
from flask import current_app

class ClaudeService:
    def __init__(self):
        # Lấy API key từ biến môi trường hoặc config
        api_key = os.getenv('ANTHROPIC_API_KEY') or current_app.config.get('ANTHROPIC_API_KEY')
        
        if not api_key:
            raise ValueError("Không tìm thấy API key của Anthropic")
        
        try:
            self.client = Anthropic(api_key=api_key)
            self.model = "claude-3-sonnet-20240229"
            self.max_tokens = 4096
        except Exception as e:
            current_app.logger.error(f"Lỗi khởi tạo Anthropic client: {str(e)}")
            raise

    def get_response(self, message, system_role=None, conversation_history=None):
        try:
            # Chuẩn bị danh sách tin nhắn
            messages = []
            
            # Thêm system role nếu có
            if system_role:
                messages.append({
                    "role": "system",
                    "content": system_role
                })
            
            # Thêm lịch sử hội thoại nếu có
            if conversation_history:
                messages.extend(conversation_history)
            
            # Thêm tin nhắn hiện tại
            messages.append({
                "role": "user",
                "content": message
            })
            
            # Gọi Claude API
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=messages
            )
            
            # Trả về nội dung phản hồi
            return response.content[0].text
        
        except Exception as e:
            current_app.logger.error(f"Lỗi khi gọi Claude API: {str(e)}")
            return f"Xin lỗi, đã có lỗi xảy ra khi xử lý yêu cầu của bạn. Chi tiết lỗi: {str(e)}"