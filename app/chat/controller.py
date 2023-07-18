from flask import Blueprint
from app.route_guard import auth_required

from app.chat.model import *
from app.chat.schema import *

chat = Blueprint('chat', __name__, url_prefix='/chat')

@chat.post('/chat')
# @auth_required()
def create_chat():
    chat = Chat.create()
    return ChatSchema().dump(chat), 201

@chat.get('/chat/<int:id>')
# @auth_required()
def get_chat(id):
    chat = Chat.get_by_id(id)
    if chat is None:
        return {'message': 'Chat not found'}, 404
    return ChatSchema().dump(chat), 200

@chat.patch('/chat/<int:id>')
# @auth_required()
def update_chat(id):
    chat = Chat.get_by_id(id)
    if chat is None:
        return {'message': 'Chat not found'}, 404
    chat.update()
    return ChatSchema().dump(chat), 200

@chat.delete('/chat/<int:id>')
# @auth_required()
def delete_chat(id):
    chat = Chat.get_by_id(id)
    if chat is None:
        return {'message': 'Chat not found'}, 404
    chat.delete()
    return {'message': 'Chat deleted successfully'}, 200

@chat.get('/chats')
# @auth_required()
def get_chats():
    chats = Chat.get_all()
    return ChatSchema(many=True).dump(chats), 200