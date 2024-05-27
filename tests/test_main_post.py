"""
Тестирования главной страницы метод POST
"""
from flaskr import db

def test_task_post(client, app):
    """
    Тестирование метод POST
    """
    response = client.post('/tasks/', data={'title': 'title', 'description': 'description'})

    with app.app_context():
        db_connection = db.getdb()
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks")
        tasks_count = len(cursor.fetchall())
        cursor.close()

    assert response.status_code == 200
