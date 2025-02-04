from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash
from app.models.bot import Bot
from app.models.system_role import SystemRole
from app import db

bot_bp = Blueprint('bot', __name__, url_prefix='/bot')

@bot_bp.route('/')
def list_bots():
    bots = Bot.query.all()
    system_roles = SystemRole.query.all()
    return render_template('bot/list.html', bots=bots, system_roles=system_roles)

@bot_bp.route('/create', methods=['GET', 'POST'])
def create_bot():
    if request.method == 'POST':
        name = request.form.get('name')
        system_role = request.form.get('system_role')
        description = request.form.get('description')

        if not name or not system_role:
            flash('Tên và System Role không được để trống', 'error')
            return redirect(url_for('bot.create_bot'))

        bot = Bot(name=name, system_role=system_role, description=description)
        db.session.add(bot)
        db.session.commit()
        
        flash('Bot đã được tạo thành công', 'success')
        return redirect(url_for('bot.list_bots'))

    system_roles = SystemRole.query.all()
    return render_template('bot/create.html', system_roles=system_roles)

@bot_bp.route('/<int:bot_id>/edit', methods=['GET', 'POST'])
def edit_bot(bot_id):
    bot = Bot.query.get_or_404(bot_id)
    
    if request.method == 'POST':
        bot.name = request.form.get('name')
        bot.system_role = request.form.get('system_role')
        bot.description = request.form.get('description')
        
        db.session.commit()
        flash('Bot đã được cập nhật thành công', 'success')
        return redirect(url_for('bot.list_bots'))

    system_roles = SystemRole.query.all()
    return render_template('bot/edit.html', bot=bot, system_roles=system_roles)

@bot_bp.route('/<int:bot_id>/delete', methods=['POST'])
def delete_bot(bot_id):
    bot = Bot.query.get_or_404(bot_id)
    db.session.delete(bot)
    db.session.commit()
    flash('Bot đã được xóa thành công', 'success')
    return redirect(url_for('bot.list_bots'))