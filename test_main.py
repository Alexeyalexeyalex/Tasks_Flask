"""
Тестирования главной страницы
"""
# from datetime import datetime
import pytest
from flaskr import create_app


@pytest.fixture()
def test_application():
    """
    Создание экземпляра приложения для тестирования
    """
    test_application = create_app()
    test_application.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield test_application

    # clean up / reset resources here


@pytest.fixture()
def client(test_application):
    """
    Создание тестового клиента для имитации возврата данных
    """
    return test_application.test_client()


@pytest.fixture()
def runner(test_application):
    """
    Изолируем приложение
    """
    return test_application.test_cli_runner()

def test_request_tasks(client):
    """
    Тестирование доступности главной страницы
    """
    response = client.get("/")
    assert response.status_code == 200

def test_json_data(client):
    """
    Тестирование метода post на возврат правильных значений
    """
    title = ""
    description = ""
    # time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = client.post("/", json={
        "title": title,
        "description":description
    })
    assert response.json["tasks"][0]["title"] == title and \
        response.json["tasks"][0]["description"] == description 
            # response.json["tasks"][id]["created_at"] == time_now and \
                # response.json["tasks"][id]["updated_at"] == time_now

def test_request_task(client):
    """
    Тестирование доступности страницы с конкретной задачей
    """
    response = client.get("/tasks/1")
    assert response.status_code == 200
