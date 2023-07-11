from app import db
from app import ma
from app.category.models import Category


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
