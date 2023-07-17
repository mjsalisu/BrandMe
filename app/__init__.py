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
from app.user.controller import user
app.register_blueprint(user)

from app.category.controller import category
app.register_blueprint(category)

from app.post.controller import post
app.register_blueprint(post)

from app.follower.controller import follower
app.register_blueprint(follower)

from app.notification.controller import notification
app.register_blueprint(notification)

from app.like.controller import like
app.register_blueprint(like)

from app.comment.controller import comment
app.register_blueprint(comment)

from app.tag.controller import tag
app.register_blueprint(tag)

from app.chat.controller import chat
app.register_blueprint(chat)

# Error handlers
from .error_handlers import *