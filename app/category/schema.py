from app import db
from app import ma
from app.user.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
