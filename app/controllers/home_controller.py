from flask import Blueprint, redirect, url_for

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    # Chuyển hướng đến trang danh sách bot
    return redirect(url_for('bot.list_bots'))