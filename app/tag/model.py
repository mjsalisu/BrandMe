from app import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False, unique=True)
    post = db.relationship("Post")
    user_one_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_one_media = db.Column(db.String, nullable=False)
    user_two_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_two_media = db.Column(db.String)
    user_three_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_three_media = db.Column(db.String)
    # users_tag = db.relationship("User", foreign_keys=[user_one_id, user_two_id, user_three_id])
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, post_id=None, user_one_id=None, user_one_media=None, user_two_id=None, user_two_media=None, user_three_id=None, user_three_media=None):
        self.post_id = post_id or self.post_id
        self.user_one_id = user_one_id or self.user_one_id
        self.user_one_media = user_one_media or self.user_one_media
        self.user_two_id = user_two_id or self.user_two_id
        self.user_two_media = user_two_media or self.user_two_media
        self.user_three_id = user_three_id or self.user_three_id
        self.user_three_media = user_three_media or self.user_three_media
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
    def get_a_post_by_id(cls, post_id):
        return cls.query.filter_by(post_id=post_id, is_deleted=False).first()
    
    @classmethod
    def get_all(cls):
        return cls.query.filter_by(is_deleted=False).all()
    
    @classmethod
    def get_by_post_id(cls, post_id):
        return cls.query.filter_by(post_id=post_id, is_deleted=False).all()
    
    @classmethod
    def create(cls, post_id, user_one_id, user_one_media):
        tag = cls(post_id=post_id, user_one_id=user_one_id, user_one_media=user_one_media)
        tag.save()
        return tag