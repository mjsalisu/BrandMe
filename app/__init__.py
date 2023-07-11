from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


@app.get('/')
def index():
    return {'status': 'ok'}


from app.user.endpoints import user
from app.category.endpoints import category
from app.feed.endpoints import feed
app.register_blueprint(user)
app.register_blueprint(category)
app.register_blueprint(feed)
