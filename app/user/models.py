from datetime import datetime
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

    def update(self):
        self.updated_at = timestamp
        db.session.commit()

    def check_password(self, password):
        return check_passwd(self.password, password)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def create(cls, name, username, password):
        user = cls(name=name, username=username, password=gen_passwd(password))
        user.save()