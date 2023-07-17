from flask import Blueprint
from app.route_guard import auth_required

from app.post.model import *
from app.post.schema import *

bp = Blueprint('post', __name__)

@bp.post('/post')
@auth_required()
def create_post():
    post = Post.create()
    return PostSchema().dump(post), 201

@bp.get('/post/<int:id>')
@auth_required()
def get_post(id):
    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404
    return PostSchema().dump(post), 200

@bp.patch('/post/<int:id>')
@auth_required()
def update_post(id):
    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404
    post.update()
    return PostSchema().dump(post), 200

@bp.delete('/post/<int:id>')
@auth_required()
def delete_post(id):
    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404
    post.delete()
    return {'message': 'Post deleted successfully'}, 200

@bp.get('/posts')
@auth_required()
def get_posts():
    posts = Post.get_all()
    return PostSchema(many=True).dump(posts), 200