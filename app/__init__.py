from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import os

# Khởi tạo database
db = SQLAlchemy()

def create_app(config_class=Config):
    # Tạo Flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    # Khởi tạo plugins
    db.init_app(app)

    from app.utils.filters import blueprint as filters_blueprint
    app.register_blueprint(filters_blueprint)

    # Import và đăng ký blueprints
    from app.controllers.home_controller import home_bp
    from app.controllers.bot_controller import bot_bp
    from app.controllers.topic_controller import topic_bp
    from app.controllers.chat_controller import chat_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(bot_bp)
    app.register_blueprint(topic_bp)
    app.register_blueprint(chat_bp)

    # Đảm bảo thư mục instance tồn tại
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Tạo database khi khởi động
    with app.app_context():
        db.create_all()

    return app