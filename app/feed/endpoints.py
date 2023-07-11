from flask import Blueprint, request
from app.feed.models import Feed
from app.feed.schema import FeedSchema

feed = Blueprint('feed', __name__, url_prefix='/feed')

@feed.post('create')
def create_feed():
    media = request.json.get('media')
    caption = request.json.get('caption')
    category_id = request.json.get('category_id')
    user_tag = request.json.get('user_tag')
    visibility = request.json.get('visibility')

    # If visibility is FALSE, then user_tag MUST be provided
    if not visibility and not user_tag:
        return {"message": 'Please provide user tag', "status": 400}

    if media and caption and category_id:
        Feed.create(media, caption, category_id, user_tag, visibility)
        return {"message": 'Feed created for successfully.', "status": 200}
    
    return {"message": 'Feed creation failed, please try again', "status": 400}
    
@feed.patch('edit/<int:feed_id>')
def edit_feed(feed_id):
    media = request.json.get('media')
    caption = request.json.get('caption')
    category_id = request.json.get('category_id')
    user_tag = request.json.get('user_tag')
    visibility = request.json.get('visibility')

    # If visibility is FALSE, then user_tag MUST be provided
    if not visibility and not user_tag:
        return {"message": 'Please provide user tag', "status": 400}

    check_feed = Feed.get_feed_by_id(feed_id=feed_id)
    if check_feed:
        Feed.edit_feed(check_feed, media=media, caption=caption, category_id=category_id, user_tag=user_tag, visibility=visibility)
        return {"message": 'Feed updated successfully', "status": 200}
    
    return {"message": 'Feed not found', "status": 400}

@feed.get('view/<int:feed_id>')
def get_feed(feed_id):
    feed = Feed.get_feed_by_id(feed_id)
    if feed:
        feed = FeedSchema().dump(feed)
        return {"feed": feed, "status": 200}
    
    return {"message": 'Feed not found', "status": 400}

@feed.get('all')
def get_all_feeds():
    feeds = Feed.query.all()
    feeds_list = FeedSchema().dump(feeds, many=True)
    return {"feeds": feeds_list, "status": 200}