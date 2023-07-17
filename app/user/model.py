from operator import or_
import jwt, string, secrets, bcrypt
from datetime import datetime
from app import app, db, secret

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable=True)
    email = db.Column(db.String, unique=True, nullable=True)
    username = db.Column(db.String, unique=True, nullable=True)
    password = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.String, nullable=True)
    cover_picture = db.Column(db.String, nullable=True)
    role = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        self.updated_at = db.func.now()
        db.session.commit()
    
    def generate_password(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        return password
    
    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
    
    def generate_token(self):
        payload = {
            'exp': app.config.get('JWT_REFRESH_TOKEN_EXPIRES'),
            'iat': datetime.utcnow(),
            'sub': self.id,
            'role': self.role
        }
        return jwt.encode(payload, secret, algorithm='HS256')
    
    def update_password(self, old_password, new_password):
        if self.is_verified(old_password):
            self.password = new_password
            self.hash_password()
            self.update()
            return True
        return False
    
    def reset_password(self, new_password):
        self.password = new_password
        self.hash_password()
        self.update()

    @classmethod
    def get_all(cls):
        return cls.query.filter_by().all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
    
    @classmethod
    def get_by_email(self, email):
        return User.query.filter(User.email==email).first()
    
    @classmethod
    def get_by_username(self, username):
        return User.query.filter(User.username==username).first()
    
    @classmethod
    def get_by_email_or_username(cls, email=None, username=None):
        return cls.query.filter(or_(cls.email==email, cls.username==username)).first()
    
    @classmethod
    def create(cls, fullname, email, username, password, profile_picture, cover_picture, role):
        user = cls(fullname=fullname, email=email, username=username, password=password, profile_picture=profile_picture, cover_picture=cover_picture, role=role)
        user.hash_password()
        user.save()
        return user