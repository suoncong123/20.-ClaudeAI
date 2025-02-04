from app.models.conversation import Conversation

class ContextService:
    def __init__(self, max_context_length=10):
        self.max_context_length = max_context_length

    def get_conversation_context(self, topic_id):
        """Lấy ngữ cảnh hội thoại cho topic"""
        conversations = Conversation.query\
            .filter_by(topic_id=topic_id)\
            .order_by(Conversation.created_at.desc())\
            .limit(self.max_context_length)\
            .all()
        
        # Đảo ngược để có thứ tự thời gian tăng dần
        conversations.reverse()
        
        context = []
        for conv in conversations:
            context.append({
                "role": conv.role,
                "content": conv.content
            })
            
        return context

    def truncate_context(self, context, max_tokens=8000):
        """Cắt bớt ngữ cảnh nếu quá dài"""
        total_tokens = 0
        truncated_context = []
        
        for message in reversed(context):
            # Ước tính số token (4 ký tự ~ 1 token)
            message_tokens = len(message['content']) // 4
            if total_tokens + message_tokens > max_tokens:
                break
                
            truncated_context.insert(0, message)
            total_tokens += message_tokens
            
        return truncated_context