"""
Тестирования страницы задания метод DELETE
"""

from flaskr import db

def test_task_delete(client, app, id=5):
    """
    Тестирование метод DELETE
    """
    client.delete(f'/tasks/{id}')
    with app.app_context():
        db_connection = db.getdb()
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM tasks WHERE id = {id}")
        task = cursor.fetchone()
        cursor.close()
        print(task)

        assert task is None
