from flask import Blueprint
from app.route_guard import auth_required

from app.like.model import *
from app.like.schema import *

bp = Blueprint('like', __name__)

@bp.post('/like')
@auth_required()
def create_like():
    like = Like.create()
    return LikeSchema().dump(like), 201

@bp.get('/like/<int:id>')
@auth_required()
def get_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    return LikeSchema().dump(like), 200

@bp.patch('/like/<int:id>')
@auth_required()
def update_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    like.update()
    return LikeSchema().dump(like), 200

@bp.delete('/like/<int:id>')
@auth_required()
def delete_like(id):
    like = Like.get_by_id(id)
    if like is None:
        return {'message': 'Like not found'}, 404
    like.delete()
    return {'message': 'Like deleted successfully'}, 200

@bp.get('/likes')
@auth_required()
def get_likes():
    likes = Like.get_all()
    return LikeSchema(many=True).dump(likes), 200