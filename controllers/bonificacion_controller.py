from flask import Blueprint, request, jsonify, render_template
from utils.database import db
from models import User, Task
from datetime import datetime
from flask_login import login_required

bonificacion_blueprint = Blueprint('bonificaciones', __name__)

@bonificacion_blueprint.route('/bonificaciones', methods=['GET'])
@login_required
def page_bonificacion():
    tasks = Task.query.all() # Recuperar todas las tareas de la base de datos
    user_task = {} # Diccionario para almacenar información de tareas por usuario

   # Procesar cada tarea
    for task in tasks:
        if task.status_id == 3:   # Verificar si la tarea está completada (status_id == 3)
            user = User.query.get(task.user_id) # Recuperar el usuario que completó la tarea
            # Inicializar la entrada del usuario en el diccionario si no está presente
            if user.id not in user_task:
                user_task[user.id] = {
                    'user': user.first_name + ' ' + user.last_name,
                    'tasks': [],
                    'done_early': 0,
                    'total_bonificacion': 0,
                    'total_dolar': 0,
                    'cycle_done_early': 0,  # Para contar tareas en el ciclo actual
                    'show_bonus_7': False,  # Para mostrar el popup de bonificación de 7
                    'show_bonus_21': False  # Para mostrar el popup de bonificación de 21
                }
            
            # Determinar el porcentaje de bonificación y la cantidad en dólares según la dificultad de la tarea
            bonus_percentage = 10 if task.difficulty == 'Easy' else 15 if task.difficulty == 'Medium' else 20
            bonus_dollar = 5 if task.difficulty == 'Easy' else 10 if task.difficulty == 'Medium' else 15
            current_bonus_dollar = bonus_dollar + (bonus_dollar * bonus_percentage / 100)
            
            # Verificar si la tarea se completó antes de tiempo
            if task.estimatetime is not None and task.donetime is not None and task.estimatetime >= task.donetime:
                user_task[user.id]['done_early'] += 1  # Incrementar el contador de tareas completadas antes de tiempo
                user_task[user.id]['cycle_done_early'] += 1 # Incrementar el contador de tareas completadas antes de tiempo en el ciclo actual
                user_task[user.id]['total_bonificacion'] += bonus_percentage # Añadir el porcentaje de bonificación al total
                user_task[user.id]['total_dolar'] += current_bonus_dollar # Añadir la cantidad de dólares de bonificación al total

                # Añadir la tarea a la lista de tareas del usuario
                user_task[user.id]['tasks'].append({
                    'task': task.description,
                    'bonificacion': bonus_percentage,
                    'dolar': current_bonus_dollar
                })

                # Mostrar bonificaciones adicionales en hitos específicos
                if user_task[user.id]['cycle_done_early'] == 7:
                    user_task[user.id]['show_bonus_7'] = True
                if user_task[user.id]['cycle_done_early'] == 21:
                    user_task[user.id]['show_bonus_21'] = True

                # Reiniciar bonificaciones y dólares si el contador de tareas antes de tiempo es mayor a 21
                if user_task[user.id]['cycle_done_early'] > 21:
                    user_task[user.id]['cycle_done_early'] = 1
                    user_task[user.id]['total_bonificacion'] = bonus_percentage
                    user_task[user.id]['total_dolar'] = current_bonus_dollar
                    user_task[user.id]['tasks'] = [{
                        'task': task.description,
                        'bonificacion': bonus_percentage,
                        'dolar': current_bonus_dollar
                    }]
                    user_task[user.id]['show_bonus_7'] = False
                    user_task[user.id]['show_bonus_21'] = False
            else:
                 # Añadir la tarea a la lista de tareas del usuario sin bonificaciones
                 #Aquí estamos añadiendo un diccionario que contiene la descripción de la tarea, el porcentaje de bonificación y 
                 #la cantidad en dólares de bonificación a la lista de tareas del usuario en el diccionario user_task.
                user_task[user.id]['tasks'].append({
                    'task': task.description,
                    'bonificacion': "",
                    'dolar': ""
                })

    # Aplicar bonificaciones adicionales por tareas completadas antes de tiempo en hitos específicos
    for user_id, details in user_task.items():
        if details['done_early'] % 21 == 7:
            additional_bonus_7 = details['total_dolar'] * 0.05  # 5% additional bonus on total dollars
            details['total_bonificacion'] += 5  # 5% additional bonus percentage
            details['total_dolar'] += additional_bonus_7  # Adjusting total dollars with the additional bonus
            details['show_bonus_7'] = True

        if details['done_early'] % 21 == 0 and details['done_early'] > 0:
            additional_bonus_21 = details['total_dolar'] * 0.10  # 10% additional bonus on total dollars
            details['total_bonificacion'] += 10  # 10% additional bonus percentage
            details['total_dolar'] += additional_bonus_21  # Adjusting total dollars with the additional bonus
            details['show_bonus_21'] = True

    total_general_dolares = sum(user['total_dolar'] for user in user_task.values())

    return render_template('bonificacion.html', user_task=user_task, total_dolares=total_general_dolares)
