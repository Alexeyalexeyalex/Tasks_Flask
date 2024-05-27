"""
Файл инициализации приложения
"""
from json import load
from flask import Flask
from .tasks import main

def create_app():
    """Создание приложения"""
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config.from_file("config.json", load=load)

    return app
