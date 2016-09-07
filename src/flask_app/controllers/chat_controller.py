# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

api = Blueprint('chat_controller', __name__, url_prefix='/chat')


# @api.route('/', methods=['GET'])
# def index():
#     return render_template("chat/index.html")
#
#
# @api.route('/main', methods=['GET'])
# def chat():
#     return render_template("chat/index.html")
#
