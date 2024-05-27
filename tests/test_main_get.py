"""
Тестирования главной страницы метод GET
"""
import json

def test_main_get(client, app, count=5):
    """
    Тестирование главной страницы
    """
    assert client.get('/').status_code == 200
    assert client.get('/tasks/').status_code == 200

    with app.app_context():
        decoded_data = client.get('/tasks/').data.decode('utf-8')
        tasks_count = len(json.loads(decoded_data)['tasks'])
    assert tasks_count == count
