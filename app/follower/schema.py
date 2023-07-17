from app import ma
from app.follower.model import *

class FollowerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Follower
        exclude = ('is_deleted',)