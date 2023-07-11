from datetime import datetime
from app import db

timestamp = datetime.now()

class Feed(db.Model):
    __tablename__ = 'feed'
    feed_id = db.Column(db.Integer, primary_key=True)
    media = db.Column(db.String, nullable=False)
    caption = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    category = db.relationship("Category")
    user_tag = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    user = db.relationship("User")
    visibility = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=timestamp)
    updated_at = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def edit_feed(self, media, caption, category_id, user_tag, visibility):
        self.media = media or self.media
        self.caption = caption or self.caption
        category_id = category_id or self.category_id
        user_tag = user_tag or self.user_tag
        visibility = visibility or self.visibility
        self.updated_at = timestamp
        db.session.commit()

    @classmethod
    def get_feed_by_id(cls, feed_id):
        return cls.query.filter_by(feed_id=feed_id).first()

    @classmethod
    def create(cls, media, caption, category_id, user_tag, visibility):
        user = cls(media=media, caption=caption, category_id=category_id, user_tag=user_tag, visibility=visibility)
        user.save()