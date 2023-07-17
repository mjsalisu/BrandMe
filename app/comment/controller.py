from flask import Blueprint
from app.route_guard import auth_required

from app.comment.model import *
from app.comment.schema import *

bp = Blueprint('comment', __name__)

@bp.post('/comment')
@auth_required()
def create_comment():
    comment = Comment.create()
    return CommentSchema().dump(comment), 201

@bp.get('/comment/<int:id>')
@auth_required()
def get_comment(id):
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    return CommentSchema().dump(comment), 200

@bp.patch('/comment/<int:id>')
@auth_required()
def update_comment(id):
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    comment.update()
    return CommentSchema().dump(comment), 200

@bp.delete('/comment/<int:id>')
@auth_required()
def delete_comment(id):
    comment = Comment.get_by_id(id)
    if comment is None:
        return {'message': 'Comment not found'}, 404
    comment.delete()
    return {'message': 'Comment deleted successfully'}, 200

@bp.get('/comments')
@auth_required()
def get_comments():
    comments = Comment.get_all()
    return CommentSchema(many=True).dump(comments), 200