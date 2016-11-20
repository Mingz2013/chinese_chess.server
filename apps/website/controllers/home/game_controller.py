# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template

api = Blueprint('game_controller', __name__, url_prefix='/game')


@api.route('/', methods=['GET'])
def index():
    return render_template("home/game/index.html")
