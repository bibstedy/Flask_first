import sqlite3
import os
from flask import Flask, render_template, request, g
from FDataBase import FDataBase

app = Flask(__name__)

# Кофигурация
DATABASE=os.path.join(app.root_path, 'bibasite.db')
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')

app.config.from_object(__name__)


# Создание БД

def connect_db():
    """Соединение с БД, записи представленны в виде словоря."""
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()

def get_db():
    """Соединение с БД, если оно еще не установлено"""
    if not hasattr(g,'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с БД, если оно было установленно"""
    if hasattr(g,'link_db'):
        g.link_db.close()

