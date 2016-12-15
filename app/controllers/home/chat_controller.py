# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

api = Blueprint('chat_controller', __name__, url_prefix='/chat')


@api.route('/', methods=['GET'])
def index():
    return render_template("home/chat/index.html")
