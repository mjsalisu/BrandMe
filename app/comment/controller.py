from flask import Blueprint
from app.route_guard import auth_required

from app.comment.model import *
from app.comment.schema import *

comment = Blueprint('comment', __name__, url_prefix='/comment')

@comment.post('/comment')
# @auth_required()
def create_comment():
    comment = Comment.create()
    return CommentSchema().dump(comment), 201

@comment.get('/comment/<int:id>')
# @auth_required()
def get_comment(id):
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    return CommentSchema().dump(comment), 200

@comment.patch('/comment/<int:id>')
# @auth_required()
def update_comment(id):
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    comment.update()
    return CommentSchema().dump(comment), 200

@comment.delete('/comment/<int:id>')
# @auth_required()
def delete_comment(id):
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    comment.delete()
    return {'message': 'Comment deleted successfully'}, 200

@comment.get('/comments')
# @auth_required()
def get_comments():
    comments = Comment.get_all()
    return CommentSchema(many=True).dump(comments), 200