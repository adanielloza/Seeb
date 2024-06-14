# controllers/reports_controller.py

from flask import Blueprint, request, jsonify, render_template
from utils.database import db
from models import User, Task, Job
from flask_login import login_required

reports_blueprint = Blueprint('reports', __name__)

@reports_blueprint.route('/report', methods=['GET'])
@login_required
def report_best_employees():
    job_id = request.args.get('job_id', type=int)
    jobs = Job.query.all()
    
    if job_id:
        selected_job = Job.query.get_or_404(job_id)
        tasks = Task.query.filter_by(job_id=selected_job.id).all()
        employees = {}
        
        for task in tasks:
            if task.status_id == 3:  # Estado 3 significa completado
                user = User.query.get(task.user_id)
                if user.id not in employees:
                    employees[user.id] = {
                        'user': user.first_name + ' ' + user.last_name,
                        'easy': 0,
                        'medium': 0,
                        'hard': 0,
                        'total': 0,
                        'score': 0  # New field to keep track of the weighted score
                    }
                
                if task.difficulty == 'Easy':
                    employees[user.id]['easy'] += 1
                    employees[user.id]['score'] += 1  # Easy task = 1 point
                elif task.difficulty == 'Medium':
                    employees[user.id]['medium'] += 1
                    employees[user.id]['score'] += 2  # Medium task = 2 points
                elif task.difficulty == 'Hard':
                    employees[user.id]['hard'] += 1
                    employees[user.id]['score'] += 3  # Hard task = 3 points
                
                employees[user.id]['total'] += 1
        
        sorted_employees = sorted(employees.values(), key=lambda e: e['score'], reverse=True)
        best_employee = sorted_employees[0] if sorted_employees else None
        report = [{
            'job_id': selected_job.id,
            'job_name': selected_job.name,
            'start_date': selected_job.initdate,
            'end_date': selected_job.enddate,
            'employees': sorted_employees
        }]
    else:
        report = []

    return render_template('best_employees_report.html', jobs=jobs, report=report, selected_job_id=job_id)
