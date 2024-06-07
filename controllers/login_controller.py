from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from utils.database import db
from models import User
from flask_login import LoginManager

# Initialize Blueprint
login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        # return redirect(url_for('main.dashboard'))
        return render_template('base.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and password == user.password:  # check_password_hash(user.password, password):
            login_user(user)
            # return redirect(url_for('main.dashboard'))  # Adjust to your main page's route
            # return redirect('Location: /users')
            return render_template('users.html', users=User.query.all())
        else:
            flash('Invalid username or password')

    return render_template('login.html')


@login_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login.login'))
