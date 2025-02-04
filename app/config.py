import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Đường dẫn tới thư mục gốc của project
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    
    # Tạo thư mục instance nếu chưa tồn tại
    instance_path = os.path.join(basedir, 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
    
    # Cấu hình cơ bản
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    
    # Đường dẫn database được định nghĩa rõ ràng
    DATABASE_PATH = os.path.join(instance_path, 'database.sqlite')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Cấu hình Claude AI
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    
    # Cấu hình ứng dụng
    MAX_CONVERSATION_LENGTH = 100
    MAX_TOPIC_PER_BOT = 50
    CODE_LANGUAGES = [
        'python', 'javascript', 'html', 'css', 'sql', 
        'bash', 'json', 'yaml', 'markdown'
    ]