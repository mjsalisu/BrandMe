from flask import Blueprint, request
from app.user.models import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.post('create')
def create_user():
    name = request.json.get('name')
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.get_by_username(username)
    if user:
        return {"message": 'Username with \'{}\' already exists'.format(username), "status": 400}
        
    if name and username and password:
        User.create(name, username, password)
        return {"message": 'Account created for successfully', "status": 200}
    
    return {"message": 'Account creation failed, please try again', "status": 400}
    

@user.post('login')
def user_login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.get_by_username(username)
    if user and user.check_password(password):
        return {"message": 'User logged in succcessful', "status": 200}
       
    return {"message": 'Invalid username or password', "status": 400}

@user.put('update')
def update_user():
    return True

@user.get('<int:user_id>')
def get_user(user_id):
    return True

@user.get('all')
def get_all_users():
    return True