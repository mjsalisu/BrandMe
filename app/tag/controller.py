from flask import Blueprint
from app.route_guard import auth_required

from app.tag.model import *
from app.tag.schema import *

bp = Blueprint('tag', __name__)

@bp.post('/tag')
@auth_required()
def create_tag():
    tag = Tag.create()
    return TagSchema().dump(tag), 201

@bp.get('/tag/<int:id>')
@auth_required()
def get_tag(id):
    tag = Tag.get_by_id(id)
    if tag is None:
        return {'message': 'Tag not found'}, 404
    return TagSchema().dump(tag), 200

@bp.patch('/tag/<int:id>')
@auth_required()
def update_tag(id):
    tag = Tag.get_by_id(id)
    if tag is None:
        return {'message': 'Tag not found'}, 404
    tag.update()
    return TagSchema().dump(tag), 200

@bp.delete('/tag/<int:id>')
@auth_required()
def delete_tag(id):
    tag = Tag.get_by_id(id)
    if tag is None:
        return {'message': 'Tag not found'}, 404
    tag.delete()
    return {'message': 'Tag deleted successfully'}, 200

@bp.get('/tags')
@auth_required()
def get_tags():
    tags = Tag.get_all()
    return TagSchema(many=True).dump(tags), 200