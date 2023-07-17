from flask import Blueprint
from app.route_guard import auth_required

from app.follower.model import *
from app.follower.schema import *

bp = Blueprint('follower', __name__)

@bp.post('/follower')
@auth_required()
def create_follower():
    follower = Follower.create()
    return FollowerSchema().dump(follower), 201

@bp.get('/follower/<int:id>')
@auth_required()
def get_follower(id):
    follower = Follower.get_by_id(id)
    if follower is None:
        return {'message': 'Follower not found'}, 404
    return FollowerSchema().dump(follower), 200

@bp.patch('/follower/<int:id>')
@auth_required()
def update_follower(id):
    follower = Follower.get_by_id(id)
    if follower is None:
        return {'message': 'Follower not found'}, 404
    follower.update()
    return FollowerSchema().dump(follower), 200

@bp.delete('/follower/<int:id>')
@auth_required()
def delete_follower(id):
    follower = Follower.get_by_id(id)
    if follower is None:
        return {'message': 'Follower not found'}, 404
    follower.delete()
    return {'message': 'Follower deleted successfully'}, 200

@bp.get('/followers')
@auth_required()
def get_followers():
    followers = Follower.get_all()
    return FollowerSchema(many=True).dump(followers), 200