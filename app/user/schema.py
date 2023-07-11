from app import db
from app import ma
from app.user.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class UsersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    user_id = ma.auto_field()
    name = ma.auto_field()
    username = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
