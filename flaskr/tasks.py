"""
Файл для обработки ссылок и методов на странице
"""
from datetime import datetime
from flask import jsonify, abort, request, Blueprint
from .db import getdb

# Необходимая настройка для выноса ссылок из файла инит
main = Blueprint('main', __name__)

@main.errorhandler(404)
def not_found(e):
    """Обработка ошибки 404 для вывода json"""
    return jsonify(error=str(e.description))

@main.errorhandler(500)
def internal_server_error(e):
    """Обработка ошибки 500 для вывода json"""
    return jsonify(error=str(e.description))

@main.errorhandler(400)
def bad_request(e):
    """Обработка ошибки 400 для вывода json"""
    return jsonify(error=str(e.description))


@main.route('/', methods=['GET'])
@main.route('/tasks/', methods=['GET'])
def get_tasks():
    """Обработка метода получения всех задач"""
    db_connection = getdb()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()

    return jsonify({'tasks': list(tasks)})

@main.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Обработка метода получения задачи по id"""
    try:
        db_connection = getdb()
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM tasks WHERE id = {task_id}")
        tasks = cursor.fetchall()
        cursor.close()

        return jsonify({'tasks': list(tasks)})
    except:
        abort(404, description="Не удалось найти задачу")


@main.route('/', methods=['POST'])
@main.route('/tasks/', methods=['POST'])
def create_task():
    """Обработка метода отправки данных со страницы"""
    if not request.json or not 'title' in request.json:
        abort(400, description="Не задан параметр title")
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        db_connection = getdb()
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(
            "INSERT INTO tasks (title, description, created_at, updated_at, done) \
                VALUES (%s, %s, %s, %s, %s)",
            (request.json['title'], request.json.get('description', ""), time_now, time_now, False)
        )
        task_id = cursor.lastrowid
        cursor.close()
        db_connection.commit()
        return get_task(task_id), 201
    except:
        abort(400, description="Неправильно заданы параметры")

@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Обработка метода изменения данных задачи по id"""
    if not request.json or not 'title' in request.json:
        abort(400, description="Не задан параметр title")
    if 'description' not in request.json:
        abort(400, description="Не задан параметр description")
    if 'done' not in request.json:
        abort(400, description="Не задан параметр done")



    time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        db_connection = getdb()
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(
            "UPDATE tasks SET title = %s, description = %s, updated_at = %s, done = %s \
                WHERE id = %s",
            (request.json['title'], request.json['description'], time_now,
                request.json['done'], task_id)
        )
        cursor.close()
        db_connection.commit()

        return  get_task(task_id), 201
    except:
        abort(404, description="Не удалось найти задачу")


@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Обработка метода удаления задачи по id"""
    try:
        db_connection = getdb()
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(f"DELETE FROM tasks WHERE id = {task_id}")
        cursor.close()
        db_connection.commit()

        return jsonify({"info":"Задача успешно удалена"})
    except:
        abort(404, description="Не удалось найти задачу")
