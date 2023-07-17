from app import ma
from app.comment.model import *

class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        exclude = ('is_deleted',)