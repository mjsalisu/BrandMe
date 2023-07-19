from app import ma
from app.like.model import *
from app.post.schema import PostSchema
from app.user.schema import UserSchema

class LikeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Like
        exclude = ('is_deleted',)

        include_relationships = True
        include_fk = True
    post = ma.Nested(PostSchema)
    user = ma.Nested(UserSchema)