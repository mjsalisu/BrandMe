from app import ma
from app.comment.model import *
from app.post.schema import PostSchema
from app.user.schema import UserSchema

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        exclude = ('is_deleted',)

        include_relationships = True
        include_fk = True
    post = ma.Nested(PostSchema)
    user = ma.Nested(UserSchema)