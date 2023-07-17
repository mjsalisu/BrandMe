from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    media = db.Column(db.String, nullable=False)
    caption = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship("Category")
    user_tag = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User")
    visibility = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, media, caption, category_id, user_tag, visibility):
        self.media = media or self.media
        self.caption = caption or self.caption
        category_id = category_id or self.category_id
        user_tag = user_tag or self.user_tag
        visibility = visibility or self.visibility
        self.updated_at = db.func.now()
        db.session.commit()
    
    def delete(self):
        self.is_deleted = True
        self.updated_at = db.func.now()
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id, is_deleted=False).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.filter_by(is_deleted=False).all()
    
    @classmethod
    def create(cls, media, caption, category_id, user_tag, visibility):
        post = cls(media=media, caption=caption, category_id=category_id, user_tag=user_tag, visibility=visibility)
        post.save()
        return post