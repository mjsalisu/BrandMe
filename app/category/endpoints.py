from flask import Blueprint, request
from app.category.models import Category
from app.category.schema import CategorySchema

category = Blueprint('category', __name__, url_prefix='/category')

@category.post('create')
def create_category():
    name = request.json.get('name')

    category = Category.get_by_name(name)
    if category:
        return {"message": 'Category with \'{}\' already exists.'.format(name), "status": 400}
       
    if name:
        Category.create(name)
        return {"message": 'Category created for successfully.', "status": 200}
    
    return {"message": 'Category creation failed, please try again', "status": 400}

@category.put('update')
def update_category():
    return True

@category.get('<int:category_id>')
def get_category(category_id):
    category = Category.get_category_id(category_id)
    if category:
        category = CategorySchema().dump(category)
        return {"category": category, "status": 200}
    
    return {"message": 'Category not found', "status": 400}

@category.get('all')
def get_all_categories():
    categories = Category.query.all()
    category_list = CategorySchema().dump(categories, many=True)
    return {"categories": category_list, "status": 200}