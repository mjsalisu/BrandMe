from app import ma
from app.category.schema import CategorySchema
from app.post.model import *
from app.user.schema import UserSchema

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        exclude = ('is_deleted',)

        include_relationships = True
        include_fk = True
    category = ma.Nested(CategorySchema)
    user = ma.Nested(UserSchema)