from flask import Blueprint, request
from app.route_guard import auth_required

from app.category.model import *
from app.category.schema import *

category = Blueprint('category', __name__, url_prefix='/category')

@category.post('/create')
# @auth_required()
def create_category():
    name = request.json.get('name')
    category = Category.create(name)
    return CategorySchema().dump(category), 201

@category.get('/category/<int:id>')
# @auth_required()
def get_category(id):
    category = Category.get_by_id(id)
    if category is None:
        return {'message': 'Category not found'}, 404
    return CategorySchema().dump(category), 200

@category.patch('/category/<int:id>')
# @auth_required()
def update_category(id):
    name = request.json.get('name')
    category = Category.get_by_id(id)
    if category is None:
        return {'message': 'Category not found'}, 404
    category.update(name)
    return CategorySchema().dump(category), 200

@category.delete('/category/<int:id>')
# @auth_required()
def delete_category(id):
    category = Category.get_by_id(id)
    if category is None:
        return {'message': 'Category not found'}, 404
    category.delete()
    return {'message': 'Category deleted successfully'}, 200

@category.get('/categorys')
# @auth_required()
def get_categorys():
    categorys = Category.get_all()
    return CategorySchema(many=True).dump(categorys), 200