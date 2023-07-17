from app import ma
from app.chat.model import *

class ChatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chat
        exclude = ('is_deleted',)