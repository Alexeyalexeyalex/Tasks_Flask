"""
Создание и настройка приложения для тестирования
"""
import pytest
from json import load
from flaskr import create_app

@pytest.fixture()
def app():
    """
    Создание экземпляра приложения для тестирования
    """
    app = create_app()
    app.config.from_file("config_test.json", load=load)

    yield app


@pytest.fixture()
def client(app):
    """
    Создание тестового клиента для имитации возврата данных
    """
    return app.test_client()


@pytest.fixture()
def runner(app):
    """
    Изолируем приложение
    """
    return app.test_cli_runner()
