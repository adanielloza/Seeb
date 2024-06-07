from flask import Blueprint, request, jsonify
from utils.database import db
from models import Job
from datetime import datetime
from flask_login import login_required
from flask import render_template

job_blueprint = Blueprint('jobs', __name__)

@job_blueprint.route('/jobs', methods=['GET'])
@login_required
def list_jobs():
    jobs = Job.query.all()
    return render_template('job.html', jobs=jobs)

@job_blueprint.route('/jobs/new', methods=['GET','POST'])
@login_required
def create_job():
    if request.method == 'GET':
        return render_template('add_job.html', jobs=Job.query.all())
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        initdate_str = request.form.get('initdate')
        enddate_str = request.form.get('enddate')

        if not all([name, description, initdate_str, enddate_str]):
            return render_template('add_job.html', jobs=Job.query.all())

        try:
            initdate = datetime.strptime(initdate_str, '%Y-%m-%d').date()
            enddate = datetime.strptime(enddate_str, '%Y-%m-%d').date()
            
            
        except ValueError:
            return render_template('add_job.html', jobs=Job.query.all())

        new_job = Job(name=name, description=description, initdate=initdate, enddate=enddate)
        db.session.add(new_job)
        db.session.commit()
        return render_template('add_job.html', jobs=Job.query.all())

@job_blueprint.route('/jobs/<int:job_id>/edit', methods=['GET','POST'])
@login_required
def update_job(job_id):
    if request.method == 'GET':
        job = Job.query.get_or_404(job_id)
        return render_template('edit_job.html', job=job)
    
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        initdate_str = request.form.get('initdate')
        enddate_str = request.form.get('enddate')
        
        job = Job.query.get_or_404(job_id)
        
        if name:
            job.name = name
        if description:
            job.description = description
        if initdate_str:
            try:
                initdate = datetime.strptime(initdate_str, '%Y-%m-%d').date()
                job.initdate = initdate
            except ValueError:
                return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400
        if enddate_str:
            try:
                enddate = datetime.strptime(enddate_str, '%Y-%m-%d').date()
                job.enddate = enddate
            except ValueError:
                return jsonify({'error': 'Invalid date format, expected YYYY-MM-DD'}), 400
        
        db.session.commit()
        return render_template('job.html', jobs=Job.query.all())

@job_blueprint.route('/jobs/<int:job_id>/delete', methods=['POST'])
@login_required
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return render_template('job.html', jobs=Job.query.all())
