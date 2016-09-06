# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

main = Blueprint('index', __name__)


@main.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
    # return render_template("h5.html")


@main.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@main.route('/chat', methods=['GET'])
def chat():
    return render_template("chat/index.html")


@main.route('/game', methods=['GET'])
def game():
    return render_template("game/index.html")
