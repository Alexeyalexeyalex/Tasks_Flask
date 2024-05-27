"""
Файл для работы с базой данных
"""

from flask import current_app, g, abort

import  mysql.connector

def getdb():
    """Подключение к бд"""
    try:
        if 'db' not in g or not g.db.is_connected():
            g.db = mysql.connector.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USERNAME'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE'],
            ssl_ca='C:/Users/2/Desktop/RestApi/ca.pem'
        )
        return g.db
    except:
        abort(500, description="Не удалось подключиться к бд")



def close_db():
    """Закрытие подключения к бд"""
    db = g.pop('db', None)

    if db is not None and db.is_connected():
        db.close()

def init_app(app):
    """Регистрация функции, которая будет вызвана при завершении контекста приложения"""
    app.teardown_appcontext(close_db)
