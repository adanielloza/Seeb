from flask import Blueprint, request, jsonify
from utils.database import db
from models import Task, User, Status
from datetime import datetime
from flask_login import login_required

task_blueprint = Blueprint('tasks', __name__)

# GET ALL TASKS
@task_blueprint.route('/api/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    task_list = [{
        'id': task.id,
        'job_id': task.job_id,
        'user_id': task.user_id,
        'description': task.description,
        'difficulty': task.difficulty,
        'estimatetime': task.estimatetime,
        'status_id': task.status_id,
        'donetime': task.donetime if task.donetime else None
    } for task in tasks]
    return jsonify(task_list), 200

# CREATE TASK
@task_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    job_id = data.get('job_id')
    user_id = data.get('user_id')
    description = data.get('description')
    difficulty = data.get('difficulty')
    estimatetime = data.get('estimatetime')

    if not all([job_id, description, estimatetime]):
        return jsonify({'error': 'Job ID, description, and estimated time are required'}), 400

    new_task = Task(job_id=job_id, user_id=user_id, description=description, difficulty=difficulty, estimatetime=estimatetime)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({
        'message': 'Task created successfully',
        'task': {
            'id': new_task.id,
            'job_id': new_task.job_id,
            'user_id': new_task.user_id,
            'description': new_task.description,
            'difficulty': new_task.difficulty,
            'estimatetime': new_task.estimatetime,
            'status_id': new_task.status_id,
            'donetime': new_task.donetime
        }
    }), 201

# GET ONE TASK
@task_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
# @login_required
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify({
        'id': task.id,
        'job_id': task.job_id,
        'user_id': task.user_id,
        'description': task.description,
        'difficulty': task.difficulty,
        'estimatetime': task.estimatetime,
        'status_id': task.status_id,
        'donetime': task.donetime.strftime('%Y-%m-%d %H:%M:%S') if task.donetime else None
    }), 200

# UPDATE TASK
@task_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
# @login_required
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)

    task.job_id = data.get('job_id', task.job_id)
    task.user_id = data.get('user_id', task.user_id)
    task.description = data.get('description', task.description)
    task.difficulty = data.get('difficulty', task.difficulty)
    task.estimatetime = data.get('estimatetime', task.estimatetime)
    task.status_id = data.get('status_id', task.status_id)

    donetime = data.get('donetime')
    if donetime:
        try:
            task.donetime = datetime.strptime(donetime, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({'error': 'Invalid date format for donetime. Use YYYY-MM-DD HH:MM:SS'}), 400

    db.session.commit()
    return jsonify({
        'message': 'Task updated successfully',
        'task': {
            'id': task.id,
            'job_id': task.job_id,
            'user_id': task.user_id,
            'description': task.description,
            'difficulty': task.difficulty,
            'estimatetime': task.estimatetime,
            'status_id': task.status_id,
            'donetime': task.donetime.strftime('%Y-%m-%d %H:%M:%S') if task.donetime else None
        }
    }), 200

# DELETE TASK
@task_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
# @login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'}), 200
