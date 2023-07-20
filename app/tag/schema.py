from app import ma
from app.post.schema import PostSchema
from app.tag.model import *

class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        exclude = ('is_deleted',)

        include_relationships = True
        include_fk = True
    post = ma.Nested(PostSchema)
