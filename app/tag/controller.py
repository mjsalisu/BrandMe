from flask import Blueprint, request
from app.route_guard import auth_required

from app.tag.model import *
from app.tag.schema import *

tag = Blueprint('tag', __name__, url_prefix='/tag')

@tag.post('/create')
# @auth_required()
def create_tag():
    data = request.json
    check_tag = Tag.get_by_name(data.get('name'))
    if check_tag is None:
        tag = Tag.create(
            post_id=data.get('post_id'),
            user_one_id=data.get('user_one_id'),
            user_one_media=data.get('user_one_media'),
        )
        return TagSchema().dump(tag), 201
    else:
        # check user_one_id to user_three_id if is not None
        if check_tag.user_two_id is None:
            check_tag.update(
                user_two_id=data.get('user_two_id'),
                user_two_media=data.get('user_two_media')
            )
            return TagSchema().dump(check_tag), 201
        elif check_tag.user_three_id is None:
            check_tag.update(
                user_three_id=data.get('user_three_id'),
                user_three_media=data.get('user_three_media')
            )
            return TagSchema().dump(check_tag), 201
        else:
            return {'message': 'Users tagged reached maximum'}, 400

@tag.get('/view/<int:id>')
# @auth_required()
def get_tag(id):
    tag = Tag.get_by_id(id)
    if tag is None:
        return {'message': 'Tag not found'}, 404
    return TagSchema().dump(tag), 200

@tag.patch('/update/<int:id>')
# @auth_required()
def update_tag(id):
    tag = Tag.get_by_id(id)
    if tag is None:
        return {'message': 'Tag not found'}, 404
    tag.update()
    return TagSchema().dump(tag), 200

@tag.get('/all')
# @auth_required()
def get_tags():
    tags = Tag.get_all()
    return TagSchema(many=True).dump(tags), 200

@tag.get('/post/<int:id>')
# @auth_required()
def get_tags_by_post(id):
    tags = Tag.get_by_post(id)
    return TagSchema(many=True).dump(tags), 200