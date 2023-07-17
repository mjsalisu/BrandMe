from flask import Blueprint
from app.route_guard import auth_required

from app.like.model import *
from app.like.schema import *

like = Blueprint('like', __name__, url_prefix='/like')

@like.post('/like')
@auth_required()
def create_like():
    like = Like.create()
    return LikeSchema().dump(like), 201

@like.get('/like/<int:id>')
@auth_required()
def get_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    return LikeSchema().dump(like), 200

@like.patch('/like/<int:id>')
@auth_required()
def update_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    like.update()
    return LikeSchema().dump(like), 200

@like.delete('/like/<int:id>')
@auth_required()
def delete_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    like.delete()
    return {'message': 'Like deleted successfully'}, 200

@like.get('/likes')
@auth_required()
def get_likes():
    likes = Like.get_all()
    return LikeSchema(many=True).dump(likes), 200