from flask import request, jsonify, Blueprint, render_template, redirect, url_for, flash
from utils.database import db
from models import User
from sqlalchemy.exc import IntegrityError
from flask_login import login_required

user_blueprint = Blueprint('user_controller', __name__)

@user_blueprint.route('/users', methods=['GET'])
@login_required
def get_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@user_blueprint.route('/users/new', methods=['GET', 'POST'])
@login_required
def create_user():
    if request.method == 'GET':
        return render_template('add_user.html')  # Muestra el formulario al usuario

    elif request.method == 'POST':
        # Asumiendo que los datos del formulario se envían como datos codificados en formulario (no JSON)
        data = request.form
        first_name = request.form.get('first_name')  # Eliminar la coma al final
        last_name = request.form.get('last_name')    # Eliminar la coma al final
        username = request.form.get('username')      # Eliminar la coma al final
        password = request.form.get('password')      # Eliminar la coma al final
        email = request.form.get('email')            # Eliminar la coma al final
        role = request.form.get('role')              # Eliminar la coma al final
        try:
            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
                role=role
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user_controller.get_users'))  # Redirigir después de la creación exitosa
        except IntegrityError:
            db.session.rollback()
            return render_template('add_user.html'), 400

#@user_blueprint.route('/users/<int:id>', methods=['GET'])
#def get_user(id):
    #user = User.query.get(id)
    #return jsonify(user.serialize())

@user_blueprint.route('/users/<int:id>/edit', methods=['GET','POST'])
def update_user(id):
    if request.method == 'GET':
       return render_template('edit_user.html', user=User.query.get(id)) 
   
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        role = request.form.get('role')
        
        user = User.query.get(id)
        if password == '':
            password = user.password
            
        if username == '':
            username = user.username
            
        if email == '':
            email = user.email
            
        if role == '':
            role = user.role
            
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.password = password
        user.email = email
        user.role = role
    
        db.session.commit()
        return render_template('edit_user.html', user = user), 200

@user_blueprint.route('/users/<int:id>/delete', methods=['POST'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user_controller.get_users'))  # Redirigir después de la eliminación exitosa 