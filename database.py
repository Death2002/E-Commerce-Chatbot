from flask_sqlalchemy import SQLAlchemy
from models import db
import os

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(24)
    db.init_app(app)

    with app.app_context():
        db.create_all()