from app import ma
from app.tag.model import *

class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        exclude = ('is_deleted',)