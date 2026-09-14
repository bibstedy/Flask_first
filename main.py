import sqlite3
import os
from bd_config import get_db
from FDataBase import FDataBase
from dotenv import load_dotenv
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort


app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

menu = []
@app.context_processor
def inject_menu():
    db = get_db()
    dbase = FDataBase(db)
    db_menu = dbase.getMenu()

    return {'db_menu': db_menu}

@app.route('/index')
@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)

# @app.route("/url/<variable>") - шаблон динамического URL
@app.route("/profile/<path:username>")
def profile(username):
    """ При указании имени через / оно будет отображено # path - ковертер может быть
     int- только цифры. float - числа с плав.точкой path - любые доступные символы в том числе и /"""
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Профиль пользователя: {username}"

@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title = "О сайте", menu = menu)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title = "Обратная связь", menu = menu)

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)

@app.route("/login", methods=["GET", "POST"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "biba" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title = "Авторизация", menu = menu)


if __name__ == '__main__':
    app.run(debug=True)
