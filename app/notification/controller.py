from flask import Blueprint
from app.route_guard import auth_required

from app.notification.model import *
from app.notification.schema import *

bp = Blueprint('notification', __name__)

@bp.post('/notification')
@auth_required()
def create_notification():
    notification = Notification.create()
    return NotificationSchema().dump(notification), 201

@bp.get('/notification/<int:id>')
@auth_required()
def get_notification(id):
    notification = Notification.get_by_id(id)
    if notification is None:
        return {'message': 'Notification not found'}, 404
    return NotificationSchema().dump(notification), 200

@bp.patch('/notification/<int:id>')
@auth_required()
def update_notification(id):
    notification = Notification.get_by_id(id)
    if notification is None:
        return {'message': 'Notification not found'}, 404
    notification.update()
    return NotificationSchema().dump(notification), 200

@bp.delete('/notification/<int:id>')
@auth_required()
def delete_notification(id):
    notification = Notification.get_by_id(id)
    if notification is None:
        return {'message': 'Notification not found'}, 404
    notification.delete()
    return {'message': 'Notification deleted successfully'}, 200

@bp.get('/notifications')
@auth_required()
def get_notifications():
    notifications = Notification.get_all()
    return NotificationSchema(many=True).dump(notifications), 200