from app import ma
from app.post.model import *

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        exclude = ('is_deleted',)