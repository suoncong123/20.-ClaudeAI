from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.topic import Topic
from app.models.bot import Bot
from app import db

topic_bp = Blueprint('topic', __name__, url_prefix='/topic')

@topic_bp.route('/bot/<int:bot_id>')
def list_topics(bot_id):
    bot = Bot.query.get_or_404(bot_id)
    topics = Topic.query.filter_by(bot_id=bot_id).all()
    return render_template('topic/list.html', bot=bot, topics=topics)

@topic_bp.route('/create/<int:bot_id>', methods=['GET', 'POST'])
def create_topic(bot_id):
    bot = Bot.query.get_or_404(bot_id)
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')

        if not name:
            flash('Tên topic không được để trống', 'error')
            return redirect(url_for('topic.create_topic', bot_id=bot_id))

        topic = Topic(name=name, description=description, bot_id=bot_id)
        db.session.add(topic)
        db.session.commit()
        
        flash('Topic đã được tạo thành công', 'success')
        return redirect(url_for('topic.list_topics', bot_id=bot_id))

    return render_template('topic/create.html', bot=bot)

@topic_bp.route('/<int:topic_id>/edit', methods=['GET', 'POST'])
def edit_topic(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    
    if request.method == 'POST':
        topic.name = request.form.get('name')
        topic.description = request.form.get('description')
        
        db.session.commit()
        flash('Topic đã được cập nhật thành công', 'success')
        return redirect(url_for('topic.list_topics', bot_id=topic.bot_id))

    return render_template('topic/edit.html', topic=topic)

@topic_bp.route('/<int:topic_id>/delete', methods=['POST'])
def delete_topic(topic_id):
    topic = Topic.query.get_or_404(topic_id)
    bot_id = topic.bot_id
    db.session.delete(topic)
    db.session.commit()
    flash('Topic đã được xóa thành công', 'success')
    return redirect(url_for('topic.list_topics', bot_id=bot_id))