from flask import Blueprint, request
from app.route_guard import auth_required

from app.like.model import *
from app.like.schema import *
from app.user.model import User
from app.post.model import Post

like = Blueprint('like', __name__, url_prefix='/like')

@like.post('/create')
# @auth_required()
def create_like():
    data = request.json
    if User.get_by_id(data.get('user_id')) is None:
        return {'message': 'User not found'}, 404
    if Post.get_by_id(data.get('post_id')) is None:
        return {'message': 'Post not found'}, 404
    like = Like.create(
        data.get('user_id'),
        data.get('post_id')
    )
    # throw notification
    return LikeSchema().dump(like), 201

@like.get('/view/<int:id>')
# @auth_required()
def get_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    return LikeSchema().dump(like), 200

@like.patch('/toggle/<int:id>')
# @auth_required()
def update_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    like.update()
    return LikeSchema().dump(like), 200

@like.get('/all')
# @auth_required()
def get_likes():
    likes = Like.get_all()
    return LikeSchema(many=True).dump(likes), 200

@like.get('/user/<int:id>')
# @auth_required()
def get_likes_by_user(id):
    likes = Like.get_by_user(id)
    return LikeSchema(many=True).dump(likes), 200

@like.get('/post/<int:id>')
# @auth_required()
def get_likes_by_post(id):
    likes = Like.get_by_post_id(id)
    return LikeSchema(many=True).dump(likes), 200