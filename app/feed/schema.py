from app import ma
from app.category.schema import CategorySchema
from app.feed.models import Feed
from app.user.schema import UserSchema


class FeedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feed

        include_relationships = True
        include_fk = True
    category = ma.Nested(CategorySchema)
    user = ma.Nested(UserSchema)