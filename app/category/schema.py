from app import ma
from app.category.model import *

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        exclude = ('is_deleted',)