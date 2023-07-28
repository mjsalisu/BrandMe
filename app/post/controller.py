from flask import Blueprint, request
from app.route_guard import auth_required

from app.post.model import *
from app.post.schema import *
from app.user.model import User
from app.category.model import Category

post = Blueprint('post', __name__, url_prefix='/post')

@post.post('/create')
@auth_required()
def create_post():
    data = request.json
    if Category.get_by_id(data.get('category_id')) is None:
        return {"message": 'Category not found', "status": 400}
    post = Post.create(
        media=data.get('media'),
        caption=data.get('caption'),
        category_id=data.get('category_id'),
        visibility=data.get('visibility'),
        hash_tag=data.get('hash_tag')
    )
    # throw notification
    return PostSchema().dump(post), 201
    
@post.get('/view/<int:id>')
@auth_required()
def get_post(id):
    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404
    return PostSchema().dump(post), 200

@post.patch('/update/<int:id>')
@auth_required()
def update_post(id):
    data = request.json

    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404

    Post.update(
        post,
        media=data.get('media'),
        caption=data.get('caption'),
        category_id=data.get('category_id'),
        visibility=data.get('visibility'),
        hash_tag=data.get('hash_tag')
    )
    return PostSchema().dump(post), 200

@post.get('/all')
@auth_required()
def get_posts():
    posts = Post.get_all()
    return PostSchema(many=True).dump(posts), 200