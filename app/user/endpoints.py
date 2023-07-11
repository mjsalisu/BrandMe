from flask import Blueprint, request
from app.user.models import User
from app.user.schema import ProfileSchema, UserSchema

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

@user.patch('edit/<int:user_id>')
def update_user(user_id):
    name = request.json.get('name')
    username = request.json.get('username')
    password = request.json.get('password')
    
    check_user = User.get_user_by_id(user_id=user_id)
    if check_user:
        User.edit_user(check_user, name=name, username=username, password=password)
        return {"message": 'User updated successfully', "status": 200}
    
    return {"message": 'User not found', "status": 400}

@user.get('view/<int:user_id>')
def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        user = ProfileSchema().dump(user)
        return {"user": user, "status": 200}
    return True

@user.get('all')
def get_all_users():
    users = User.query.all()
    users_list = UserSchema().dump(users, many=True)
    return {"users": users_list, "status": 200}