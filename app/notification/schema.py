from app import ma
from app.notification.model import *

class NotificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Notification
        exclude = ('is_deleted',)