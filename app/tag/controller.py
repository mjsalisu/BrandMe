from flask import Blueprint, request
from app.post.model import Post
from app.route_guard import auth_required

from app.tag.model import *
from app.tag.schema import *

tag = Blueprint('tag', __name__, url_prefix='/tag')

@tag.post('/create')
@auth_required()
def create_tag():
    data = request.json
    if Post.get_by_id(data.get('post_id')) is None:
        return {'message': 'Post not found'}, 404
    post_tag_exits = Tag.get_a_post_by_id(data.get('post_id'))

    if post_tag_exits is None:
        tag = Tag.create(
            post_id=data.get('post_id'),
            user_one_id=data.get('user_one_id'),
            user_one_media=data.get('user_one_media'),
        )
        return TagSchema().dump(tag), 200
    
    return {'message': 'Tag already exist for this post, use update instead'}, 400

@tag.get('/view/<int:id>')
@auth_required()
def get_tag(id):
    tag = Tag.get_by_id(id)
    if tag is None:
        return {'message': 'Tag not found'}, 404
    return TagSchema().dump(tag), 200

@tag.patch('/update/<int:id>')
@auth_required()
def update_tag(id):
    data = request.json
    tag = Tag.get_by_id(id)
    if tag is None:
        return {'message': 'Tag not found'}, 404
    if data.get('user_one_id') is not None:
        return {'message': 'user_one_id cannot be updated'}, 400
    
    if tag.user_two_id is None and data.get('user_two_id') is not None:
        Tag.update(
            tag,
            user_two_id=data.get('user_two_id'),
            user_two_media=data.get('user_two_media'),
        )
        return TagSchema().dump(tag), 200
    elif tag.user_three_id is None and data.get('user_three_id') is not None:
        Tag.update(
            tag,
            user_three_id=data.get('user_three_id'),
            user_three_media=data.get('user_three_media'),
        )
        return TagSchema().dump(tag), 200
    else:
        return {'message': 'users cannot be updated'}, 400

@tag.get('/all')
@auth_required()
def get_tags():
    tags = Tag.get_all()
    return TagSchema(many=True).dump(tags), 200

@tag.get('/post/<int:id>')
@auth_required()
def get_tags_by_post(id):
    tags = Tag.get_by_post_id(id)
    return TagSchema(many=True).dump(tags), 200