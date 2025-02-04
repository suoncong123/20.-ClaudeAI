from app import db
from datetime import datetime

class Bot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    system_role = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship với Topic
    topics = db.relationship('Topic', backref='bot', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Bot {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'system_role': self.system_role,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'topic_count': len(self.topics)
        }