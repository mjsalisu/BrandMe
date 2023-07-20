from flask import Blueprint, request
from app.notification.model import Notification
from app.route_guard import auth_required

from app.comment.model import *
from app.comment.schema import *
from app.user.model import User
from app.post.model import Post

comment = Blueprint('comment', __name__, url_prefix='/comment')

@comment.post('/create')
# @auth_required()
def create_comment():
    data = request.json
    if User.get_by_id(data.get('user_id')) is None:
        return {"message": 'User not found', "status": 400}
    if Post.get_by_id(data.get('post_id')) is None:
        return {"message": 'Post not found', "status": 400}
    comment = Comment.create(
        text=data.get('text'),
        user_id=data.get('user_id'),
        post_id=data.get('post_id')
    )
    return CommentSchema().dump(comment), 201

@comment.get('/view/<int:id>')
# @auth_required()
def get_comment(id):
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    return CommentSchema().dump(comment), 200

@comment.patch('/update/<int:id>')
# @auth_required()
def update_comment(id):
    data = request.json
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    Comment.update(
        comment,
        text=data.get('text')
    )
    return CommentSchema().dump(comment), 200

@comment.get('/all')
# @auth_required()
def get_comments():
    comments = Comment.get_all()
    return CommentSchema(many=True).dump(comments), 200

@comment.get('/post/<int:id>')
# @auth_required()
def get_comments_by_post(id):
    comments = Comment.get_by_user_id(id)
    return CommentSchema(many=True).dump(comments), 200

@comment.get('/user/<int:id>')
# @auth_required()
def get_comments_by_user(id):
    comments = Comment.get_by_user_id(id)
    return CommentSchema(many=True).dump(comments), 200