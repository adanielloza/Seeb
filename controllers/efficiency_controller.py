from flask import Blueprint, request, jsonify, render_template
from utils.database import db
from models import User, Task, Job
from datetime import datetime
from flask_login import login_required

efficiency_blueprint = Blueprint('efficiency', __name__)

@efficiency_blueprint.route('/efficiency', methods=['GET', 'POST'])
@login_required
def calculate_efficiency():
    job_efficiency = []
    best_job = None
    error = None

    if request.method == 'POST':
        start_date_str = request.form.get('start_date')
        end_date_str = request.form.get('end_date')

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            error = "Invalid date format. Please use YYYY-MM-DD."
            return render_template('efficiency.html', job_efficiency=job_efficiency, best_job=best_job, error=error)

        jobs = Job.query.filter(Job.initdate >= start_date, Job.enddate <= end_date).all()

        for job in jobs:
            tasks = Task.query.filter_by(job_id=job.id, status_id=3).all()
            total_tasks = len(tasks)
            if total_tasks == 0:
                continue

            tasks_in_time = [task for task in tasks if task.estimatetime >= task.donetime]
            efficiency = len(tasks_in_time) / total_tasks * 100

            user_task_count = {}
            for task in tasks_in_time:
                if task.user_id not in user_task_count:
                    user_task_count[task.user_id] = 0
                user_task_count[task.user_id] += 1

            best_worker_id = max(user_task_count, key=user_task_count.get) if user_task_count else None
            best_worker = User.query.get(best_worker_id) if best_worker_id else None

            job_efficiency.append({
                'job': job,
                'efficiency': efficiency,
                'best_worker': best_worker,
                'best_worker_tasks': user_task_count.get(best_worker_id, 0)
            })

        if job_efficiency:
            best_job = max(job_efficiency, key=lambda x: x['efficiency'])

    return render_template('efficiency.html', job_efficiency=job_efficiency, best_job=best_job, error=error)
