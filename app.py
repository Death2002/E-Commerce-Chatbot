from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Product, ChatSession, ChatMessage
from database import init_db
from chatbot import ChatBot
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
init_db(app)
chatbot = ChatBot(api_key=os.getenv('ANTHROPIC_API_KEY'))

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/register_page')
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/login_page')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        return redirect(url_for('index'))
    else:
        return render_template('login.html', error='Invalid username or password')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/chat_page')
def chat_page():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    if 'user_id' not in session:
        return jsonify({'error': 'User not logged in'}), 401

    user_id = session['user_id']
    message = request.json.get('message')

    chat_session = ChatSession.query.filter_by(user_id=user_id).order_by(ChatSession.id.desc()).first()

    if not chat_session:
        chat_session = ChatSession(user_id=user_id)
        db.session.add(chat_session)
        db.session.commit()

    chat_message = ChatMessage(session_id=chat_session.id, user_id=user_id, message=message, is_bot=False)
    db.session.add(chat_message)
    db.session.commit()

    bot_response = chatbot.process_message(message)

    bot_message = ChatMessage(session_id=chat_session.id, user_id=user_id, message=bot_response, is_bot=True)
    db.session.add(bot_message)
    db.session.commit()

    return jsonify({'response': bot_response})

@app.route('/reset_chat', methods=['POST'])
def reset_chat():
    if 'user_id' not in session:
        return jsonify({'error': 'User not logged in'}), 401

    user_id = session['user_id']
    new_session = ChatSession(user_id=user_id)
    db.session.add(new_session)
    db.session.commit()

    return jsonify({'message': 'Chat session reset successfully'}), 200
