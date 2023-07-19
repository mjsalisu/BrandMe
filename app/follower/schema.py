from app import ma
from app.follower.model import *
from app.user.schema import UserSchema

class FollowerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Follower
        exclude = ('is_deleted',)

        include_relationships = True
        include_fk = True
    follower_profile = ma.Nested(UserSchema)