from app import db

class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    followed_profile = db.relationship("User")
    is_following = db.Column(db.Boolean, default=True)
    followed_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        self.is_following = not self.is_following
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
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id, is_deleted=False).all()
    
    @classmethod
    def create(cls, user_id, followed_id):
        follower = cls(user_id=user_id, followed_id=followed_id)
        follower.save()
        return follower