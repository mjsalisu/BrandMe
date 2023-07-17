from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

# App Config
app = Flask(__name__, )
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


# Celery
from app.celery import make_celery
celery = make_celery(app)

# Database
from config import secret
app.secret_key = secret
migrate = Migrate(app, db)


# Controllers
from app.user.controller import bp as user_bp
app.register_blueprint(user_bp)
from app.post.controller import bp as post_bp
app.register_blueprint(post_bp)
from app.follower.controller import bp as follower_bp
app.register_blueprint(follower_bp)
from app.notification.controller import bp as notification_bp
app.register_blueprint(notification_bp)
from app.like.controller import bp as like_bp
app.register_blueprint(like_bp)
from app.comment.controller import bp as comment_bp
app.register_blueprint(comment_bp)
from app.tag.controller import bp as tag_bp
app.register_blueprint(tag_bp)
from app.chat.controller import bp as chat_bp
app.register_blueprint(chat_bp)

# Error handlers
from .error_handlers import *