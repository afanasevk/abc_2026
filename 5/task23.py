# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов

from flask import Flask

app = Flask(__name__)


@app.route('/about')
def about():
    return 'О компании'


@app.route('/contacts')
def contacts():
    return 'Контакты'


@app.route('/posts')
def posts():
    return 'Список постов'


if __name__ == '__main__':
    app.run(debug=True)
    