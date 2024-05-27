"""
Тестирования страницы задания метод PUT
"""
import json
from flaskr import db


def test_task_put(client, app, id=2):
    """
    Тестирование метод PUT
    """
    assert client.get(f'/tasks/{id}').status_code == 200

    client.put(f'/tasks/{id}/', data=json.dumps({"title": "title", \
                                                 "description": "description", "done":1}), \
                                            content_type="application/json")
    with app.app_context():
        db_connection = db.getdb()
        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM tasks WHERE id = {id}")
        tasks_done = cursor.fetchone()["done"]
        cursor.close()

        assert tasks_done == 1
