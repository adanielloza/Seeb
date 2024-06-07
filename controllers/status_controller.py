from flask import Blueprint, request, jsonify
from utils.database import db
from models import Status
from flask_login import login_required

status_blueprint = Blueprint('status', __name__)

@status_blueprint.route('/status', methods=['GET'])
def list_status():
    all_status = Status.query.all()
    return jsonify([status.serialize() for status in all_status]), 200

@status_blueprint.route('/status/new', methods=['POST'])
def create_status():
    data = request.get_json()
    if not data or 'status_description' not in data or 'time' not in data:
        return jsonify({'error': 'Missing data'}), 400
    status_description = data['status_description']
    time = data['time']
    new_status = Status(status_description=status_description, time=time)
    db.session.add(new_status)
    db.session.commit()
    return jsonify(new_status.serialize()), 201

@status_blueprint.route('/status/<int:status_id>', methods=['GET'])
def get_status(status_id):
    status = Status.query.get_or_404(status_id)
    return jsonify(status.serialize()), 200

@status_blueprint.route('/status/<int:status_id>/edit', methods=['PUT'])
def update_status(status_id):
    status = Status.query.get_or_404(status_id)
    data = request.get_json()
    if 'status_description' in data:
        status.status_description = data['status_description']
    if 'time' in data:
        status.time = data['time']
    db.session.commit()
    return jsonify(status.serialize()), 200

@status_blueprint.route('/status/<int:status_id>/delete', methods=['DELETE'])
def delete_status(status_id):
    status = Status.query.get_or_404(status_id)
    db.session.delete(status)
    db.session.commit()
    return jsonify({'success': 'Status deleted'}), 200
