from flask import Blueprint, request
from app.route_guard import auth_required

from app.category.model import *
from app.category.schema import *

category = Blueprint('category', __name__, url_prefix='/category')

@category.post('/create')
# @auth_required()
def create_category():
    data = request.json
    if Category.get_by_name(data.get('name')) is not None:
        return {'message': 'Category already exists'}, 400
    category = Category.create(data.get('name'))
    return CategorySchema().dump(category), 201

@category.get('/view/<int:id>')
# @auth_required()
def get_category(id):
    category = Category.get_by_id(id)
    if category is None:
        return {'message': 'Category not found'}, 404
    return CategorySchema().dump(category), 200

@category.patch('/update/<int:id>')
# @auth_required()
def update_category(id):
    data = request.json
    category = Category.get_by_id(id)
    if category is None:
        return {'message': 'Category not found'}, 404
    Category.update(category, data.get('name'))
    return CategorySchema().dump(category), 200


@category.get('/all')
# @auth_required()
def get_categorys():
    categorys = Category.get_all()
    return CategorySchema(many=True).dump(categorys), 200