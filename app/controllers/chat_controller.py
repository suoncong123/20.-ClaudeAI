from flask import Blueprint, render_template, request, jsonify
from app.models.conversation import Conversation
from app.models.topic import Topic
from app.models.bot import Bot
from app.services.claude_service import ClaudeService
from app.services.code_service import CodeService
from app import db

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/topic/<int:topic_id>')
def chat_room(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    bot = Bot.query.get(topic.bot_id)
    conversations = Conversation.get_chat_history(topic_id)
    return render_template('chat/room.html', topic=topic, bot=bot, conversations=conversations)

@chat_bp.route('/send', methods=['POST'])
def send_message():
    data = request.json
    topic_id = data.get('topic_id')
    message = data.get('message')
    
    topic = Topic.query.get_or_404(topic_id)
    bot = Bot.query.get(topic.bot_id)

    # Lưu tin nhắn người dùng
    user_message = Conversation(
        topic_id=topic_id,
        role='user',
        content=message
    )
    db.session.add(user_message)
    db.session.commit()

    # Gọi Claude API để lấy phản hồi
    claude_service = ClaudeService()
    response = claude_service.get_response(message, bot.system_role)

    # Xử lý code trong phản hồi
    code_service = CodeService()
    response, has_code = code_service.process_code_blocks(response)

    # Lưu phản hồi của bot
    bot_message = Conversation(
        topic_id=topic_id,
        role='assistant',
        content=response,
        has_code=has_code
    )
    db.session.add(bot_message)
    db.session.commit()

    return jsonify({
        'status': 'success',
        'response': response
    })

@chat_bp.route('/history/<int:topic_id>')
def get_history(topic_id):
    conversations = Conversation.get_chat_history(topic_id)
    return jsonify([conv.to_dict() for conv in conversations])