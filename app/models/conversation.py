from app import db
from datetime import datetime

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # 'user' hoặc 'assistant'
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    has_code = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Conversation {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'topic_id': self.topic_id,
            'role': self.role,
            'content': self.content,
            'created_at': self.created_at.isoformat(),
            'has_code': self.has_code
        }

    @staticmethod
    def get_chat_history(topic_id, limit=50):
        return Conversation.query\
            .filter_by(topic_id=topic_id)\
            .order_by(Conversation.created_at.desc())\
            .limit(limit)\
            .all()