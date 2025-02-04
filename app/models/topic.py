from app import db
from datetime import datetime

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    bot_id = db.Column(db.Integer, db.ForeignKey('bot.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship với Conversation
    conversations = db.relationship('Conversation', backref='topic', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Topic {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'bot_id': self.bot_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'message_count': len(self.conversations)
        }