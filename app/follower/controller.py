from flask import Blueprint, request
from app.route_guard import auth_required

from app.follower.model import *
from app.follower.schema import *
from app.user.model import User

follower = Blueprint('follower', __name__, url_prefix='/follower')

@follower.post('/create')
@auth_required()
def create_follower():
    data = request.json
    if User.get_by_id(data.get('user_id')) is None:
        return {"message": 'User not found', "status": 400}
    if User.get_by_id(data.get('followed_id')) is None:
        return {"message": 'Follower not found', "status": 400}
    # Follower not found
    follower = Follower.create(
        user_id=data.get('user_id'),
        followed_id=data.get('followed_id')
    )
    return FollowerSchema().dump(follower), 201

@follower.get('/view/<int:id>')
@auth_required()
def get_follower(id):
    follower = Follower.get_by_id(id)
    if follower is None:
        return {'message': 'Follower not found'}, 404
    return FollowerSchema().dump(follower), 200

@follower.patch('/toggle/<int:id>')
@auth_required()
def update_follower(id):
    follower = Follower.get_by_id(id)
    if follower is None:
        return {'message': 'Follower not found'}, 404
    follower.update()
    return FollowerSchema().dump(follower), 200

@follower.get('/all')
@auth_required()
def get_followers():
    followers = Follower.get_all()
    return FollowerSchema(many=True).dump(followers), 200

@follower.get('/user/<int:id>')
@auth_required()
def get_followers_by_user(id):
    followers = Follower.get_by_user_id(id)
    return FollowerSchema(many=True).dump(followers), 200