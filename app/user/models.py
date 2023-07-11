from datetime import datetime
from operator import or_
from app import db
from werkzeug.security import check_password_hash as check_passwd
from werkzeug.security import generate_password_hash as gen_passwd

timestamp = datetime.now()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, default=timestamp)
    updated_at = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def edit_user(self, name=None, username=None, password=None):
        self.name = name or self.name
        self.username = username or self.username
        self.password = gen_passwd(password) or self.password
        self.updated_at = timestamp
        db.session.commit()

    def check_password(self, password):
        return check_passwd(self.password, password)
    
    def update_profile(self, name, username, password):
        return True
    
    @classmethod
    def get_by_username_or_id(cls, username=None, user_id=None):
        return cls.query.filter(or_(cls.username==username, cls.user_id==user_id)).first()
    
    @classmethod
    def get_user_by_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def create(cls, name, username, password):
        user = cls(name=name, username=username, password=gen_passwd(password))
        user.save()