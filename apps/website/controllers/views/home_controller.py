# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template


api = Blueprint('home_controller', __name__, url_prefix='')


@api.route('/', methods=['GET'])
def index():
    return render_template("home/index.html")


@api.route('/chat', methods=['GET'])
def chat():
    return render_template("chat.html")


@api.route('/blog', methods=['GET'])
def blog():
    return render_template("blog.html")


@api.route('/game', methods=['GET'])
def game():
    return render_template("game.html")


@api.route('/about', methods=['GET'])
def about():
    return render_template("home/about.html")


@api.route('/contact', methods=['GET'])
def contact():
    return render_template("home/contact.html")


@api.route('/debug', methods=['GET'])
def debug():
    return render_template("home/debug.html")
