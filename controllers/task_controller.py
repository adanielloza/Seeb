from flask import Blueprint, request, jsonify
from utils.database import db
from models import Task, User, Status
from datetime import datetime
from flask_login import login_required
from flask import render_template

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['GET'])
@login_required
def list_tasks():
    tasks = Task.query.all()
    return render_template('task.html', tasks=tasks)

@task_blueprint.route('/tasks/new', methods=['GET','POST'])
def create_task():
    if request.method == 'GET':
        users = User.query.filter_by(role='ROLE_USER').all()
        return render_template('add_task.html', tasks=Task.query.all(), users=users)
    
    if request.method == 'POST':

        job_id = request.form.get('job_id')
        user_id = request.form.get('user_id')
        description = request.form.get('description')
        difficulty = request.form.get('difficulty')
        estimatetime = request.form.get('estimatetime')

        if not all([job_id, description, estimatetime]):
            return render_template('add_task.html', tasks=Task.query.all())

        new_task = Task(job_id=job_id, user_id=user_id, description=description, difficulty=difficulty, estimatetime=estimatetime)
        db.session.add(new_task)
        db.session.commit()
        return render_template('add_task.html', tasks=Task.query.all())

@task_blueprint.route('/tasks/<int:task_id>/edit', methods=['GET','POST'])
def update_task(task_id):
    if request.method == 'GET':
        users = User.query.filter_by(role='ROLE_USER').all()
        task = Task.query.get_or_404(task_id)
        return render_template('edit_task.html', task=task, users=users, status=Status.query.all())
    
    if request.method == 'POST':
        job_id = request.form.get('job_id')
        user_id = request.form.get('user_id')
        description = request.form.get('description')
        difficulty = request.form.get('difficulty')
        estimatetime = request.form.get('estimatetime')
        status = request.form.get('status')
        donetime = request.form.get('donetime')
        
        task = Task.query.get_or_404(task_id)
        
        task.job_id = job_id
        task.user_id = user_id
        task.description = description
        task.difficulty = difficulty
        task.estimatetime = estimatetime
        task.status_id = status
        status = int(status)
        if status == 3:
            task.donetime = donetime
            
        db.session.commit()
        return render_template('edit_task.html', task=task)

@task_blueprint.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return render_template('task.html', tasks=Task.query.all())


