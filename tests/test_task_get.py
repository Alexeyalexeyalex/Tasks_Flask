"""
Тестирования страницы задания метод GET
"""
import json

def test_task_get(client, app, id=1):
    """
    Тестирование метод GET
    """
    assert client.get('/tasks/1').status_code == 200
    assert client.get('/tasks/999999999').status_code == 200

    with app.app_context():
    #     db_connection = db.getdb()
    #     cursor = db_connection.cursor(dictionary=True)
    #     cursor.execute(f"SELECT * FROM tasks WHERE id = {id}")
    #     task = cursor.fetchall()
    #     cursor.close()
        decoded_data = client.get(f'/tasks/{id}').data.decode('utf-8')
        task_title = json.loads(decoded_data)['tasks'][0]["title"]

    assert task_title == f"Title {id}"
    