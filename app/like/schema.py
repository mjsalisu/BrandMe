from app import ma
from app.like.model import *

class LikeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Like
        exclude = ('is_deleted',)