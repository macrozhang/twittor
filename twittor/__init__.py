from flask import Flask 
from twittor.route import index, login #引入方法


def create_app():
    app = Flask(__name__)
    # app.add_url_rule('/','index', index) #   （'位置','名字', 方法) #没加url_for()
    app.add_url_rule('/index','index', index) #   （'位置','名字', 方法)
    app.add_url_rule('/login','login',login, methods=['GET','POST'])
    return app