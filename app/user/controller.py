from flask import Blueprint, g, jsonify, request

from app.user.model import User
from app.user.schema import UserSchema
from app.route_guard import auth_required
user = Blueprint('user', __name__)

@user.post('/login')
def login():
    data = request.json
    email = data.get('email')
    user = User.get_by_email(email)
    
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    if not user.check_password(data.get('password')):
        return jsonify({'message': 'Wrong password'}), 401
    # generate token
    token = user.generate_token()
    return jsonify({'token': token, 'user': UserSchema().dump(user)}), 200

@user.patch('/reset-password')
@auth_required()
def reset_password():
    new_password = request.json.get('password')
    if not new_password:
        return jsonify({'message': 'Password is required'}), 400
    elif len(new_password) < 6:
        return jsonify({'message': 'Password must be at least 6 characters'}), 400
    g.user.reset_password(new_password)
    return jsonify({'message': 'Password updated successfully'}), 200
    

@user.post('/register')
def register():
    data = request.json
    user = User.get_by_email_or_username(data.get('email'), data.get('username'))
    if user is not None:
        return jsonify({'message': 'User already exists'}), 400
    user = User.create(
        data.get('fullname'),
        data.get('email'),
        data.get('username'),
        data.get('password'),
        data.get('profile_picture'),
        data.get('cover_picture'),
        data.get('role')
        )
    if user is not None:
        return jsonify({'message': 'User created'}), 201
    return jsonify({'message': 'User not created'}), 400

@user.get('/profile/<int:id>')
@auth_required()
def get_user(id):
    user = User.get_by_id(id)
    if user is None:
        return {'message': 'User not found'}, 404
    return UserSchema().dump(user), 200

@user.patch('/setting/<int:id>')
@auth_required()
def update_user(id):
    user = User.get_by_id(id)
    if user is None:
        return {'message': 'User not found'}, 404
    data = request.json
    User.update(
        user,
        fullname=data.get('fullname'),
        email=data.get('email'),
        username=data.get('username'),
        profile_picture=data.get('profile_picture'),
        cover_picture=data.get('cover_picture'),
        role=data.get('role')
    )
    return UserSchema().dump(user), 200

# @user.delete('/delete/<int:id>')
@auth_required()
# def delete_user(id):
#     user = User.get_by_id(id)
#     if user is None:
#         return {'message': 'User not found'}, 404
#     User.delete()
#     return {'message': 'User deleted successfully'}, 200

@user.get('/users')
@auth_required()
def get_users():
    users = User.get_all()
    return UserSchema(many=True).dump(users), 200