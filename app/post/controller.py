from flask import Blueprint, request
from app.route_guard import auth_required

from app.post.model import *
from app.post.schema import *

bp = Blueprint('post', __name__)

@bp.post('/create')
@auth_required()
def create_post():
    media = request.json.get('media')
    caption = request.json.get('caption')
    category_id = request.json.get('category_id')
    visibility = request.json.get('visibility')
    user_tag = request.json.get('user_tag')

    # If visibility is FALSE, then user_tag MUST be provided
    if not visibility and not user_tag:
        return {"message": 'Please provide user tag', "status": 400}

    if media and caption and category_id:
        post = Post.create(media, caption, category_id, user_tag, visibility)
        return PostSchema().dump(post), 201
        # return {"message": 'Feed created for successfully.', "status": 200}
    else:
        return {"message": 'Please provide all required fields', "status": 400}

@bp.get('/post/<int:id>')
@auth_required()
def get_post(id):
    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404
    return PostSchema().dump(post), 200

@bp.patch('/post/<int:id>')
@auth_required()
def update_post(id):
    media = request.json.get('media')
    caption = request.json.get('caption')
    category_id = request.json.get('category_id')
    user_tag = request.json.get('user_tag')
    visibility = request.json.get('visibility')

    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404
    
    # If visibility is FALSE, then user_tag MUST be provided
    if not visibility and not user_tag:
        return {"message": 'Please provide user tag', "status": 400}

    Post.update(id, media=media, caption=caption, category_id=category_id, user_tag=user_tag, visibility=visibility)
    return PostSchema().dump(post), 200
    # return {"message": 'Post updated successfully', "status": 200}
    

@bp.delete('/post/<int:id>')
@auth_required()
def delete_post(id):
    post = Post.get_by_id(id)
    if post is None:
        return {'message': 'Post not found'}, 404
    post.delete()
    return {'message': 'Post deleted successfully'}, 200

@bp.get('/posts')
@auth_required()
def get_posts():
    posts = Post.get_all()
    return PostSchema(many=True).dump(posts), 200