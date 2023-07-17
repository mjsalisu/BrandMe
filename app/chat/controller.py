from flask import Blueprint
from app.route_guard import auth_required

from app.chat.model import *
from app.chat.schema import *

bp = Blueprint('chat', __name__)

@bp.post('/chat')
@auth_required()
def create_chat():
    chat = Chat.create()
    return ChatSchema().dump(chat), 201

@bp.get('/chat/<int:id>')
@auth_required()
def get_chat(id):
    chat = Chat.get_by_id(id)
    if chat is None:
        return {'message': 'Chat not found'}, 404
    return ChatSchema().dump(chat), 200

@bp.patch('/chat/<int:id>')
@auth_required()
def update_chat(id):
    chat = Chat.get_by_id(id)
    if chat is None:
        return {'message': 'Chat not found'}, 404
    chat.update()
    return ChatSchema().dump(chat), 200

@bp.delete('/chat/<int:id>')
@auth_required()
def delete_chat(id):
    chat = Chat.get_by_id(id)
    if chat is None:
        return {'message': 'Chat not found'}, 404
    chat.delete()
    return {'message': 'Chat deleted successfully'}, 200

@bp.get('/chats')
@auth_required()
def get_chats():
    chats = Chat.get_all()
    return ChatSchema(many=True).dump(chats), 200