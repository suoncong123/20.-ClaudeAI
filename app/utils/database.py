from app import db
from sqlalchemy import text

def init_db():
    """Khởi tạo database và tạo bảng"""
    db.create_all()

def reset_db():
    """Reset toàn bộ database"""
    db.drop_all()
    db.create_all()

def get_db_stats():
    """Lấy thống kê cơ bản về database"""
    stats = {}
    
    # Đếm số lượng bot
    stats['bot_count'] = db.session.execute(text("SELECT COUNT(*) FROM bot")).scalar()
    
    # Đếm số lượng topic
    stats['topic_count'] = db.session.execute(text("SELECT COUNT(*) FROM topic")).scalar()
    
    # Đếm số lượng conversation
    stats['conversation_count'] = db.session.execute(text("SELECT COUNT(*) FROM conversation")).scalar()
    
    return stats

def backup_db():
    """Tạo backup database"""
    # TODO: Implement database backup logic
    pass

def vacuum_db():
    """Tối ưu hóa database"""
    db.session.execute(text("VACUUM"))
    db.session.commit()