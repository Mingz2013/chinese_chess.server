# -*- coding:utf-8 -*-
__author__ = 'zhaojm'



from flask import Blueprint, render_template

main = Blueprint('index', __name__)  # url_prefix='/h5'


@main.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
    # return render_template("h5.html")


@main.route('/', methods=['GET'])
@main.route('/h5/', methods=['GET'])
def index():
    return render_template("index.html")


    # @main.route('/debug/', methods=['GET'])
    # def h5_debug():
    #     return render_template("debug.html")
