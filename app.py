from flask import Flask 
from utils.database import db
from models import User  # Import the User class
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'a_default_secret_key_for_development')

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login.login'  # Assuming 'login' blueprint has a 'login' route

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all() 

# Import the controllers

# Import the usuario blueprint
from controllers import user_blueprint
app.register_blueprint(user_blueprint)

# Import the login blueprint
from controllers import login_blueprint
app.register_blueprint(login_blueprint)

# Import the job blueprint
from controllers import job_blueprint
app.register_blueprint(job_blueprint)

# Import the task blueprint
from controllers import task_blueprint
app.register_blueprint(task_blueprint)

# Import the bonificacion blueprint
from controllers import bonificacion_blueprint
app.register_blueprint(bonificacion_blueprint)

# Import the status blueprint
from controllers import status_blueprint
app.register_blueprint(status_blueprint)

# Import the reports blueprint
from controllers import reports_blueprint
app.register_blueprint(reports_blueprint)

# Import the efficiency blueprint
from controllers import efficiency_blueprint
app.register_blueprint(efficiency_blueprint)





if __name__ == "__main__":
    app.run(debug=True)

