# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

main = Blueprint('index_controller', __name__)


@main.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
    # return render_template("h5.html")


@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@main.route('/chat', methods=['GET'])
def chat():
    return render_template("chat.html")


@main.route('/blog', methods=['GET'])
def blog():
    return render_template("blog.html")


@main.route('/game', methods=['GET'])
def game():
    return render_template("game.html")


@main.route('/admin', methods=['GET'])
def admin():
    return render_template("admin.html")
