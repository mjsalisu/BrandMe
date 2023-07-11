from datetime import datetime
from app import db

timestamp = datetime.now()

class Category(db.Model):
    __tablename__ = 'category'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=timestamp)
    updated_at = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.updated_at = timestamp
        db.session.commit()

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def create(cls, name):
        user = cls(name=name)
        user.save()