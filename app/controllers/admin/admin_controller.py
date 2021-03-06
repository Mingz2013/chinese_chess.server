# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Blueprint, render_template, url_for, redirect

from ...services.views.admin_service import AdminService

api = Blueprint('admin_controller', __name__, url_prefix='/admin')


@api.route('/', methods=['GET'])
def index():
    if AdminService.check_is_need_init():
        return redirect(url_for('init_controller.index'))
    if not AdminService.check_is_login():
        return redirect(url_for('.login'))
    return render_template("admin/index.html")


@api.route('/chat', methods=['GET'])
def chat():
    return render_template("admin/chat/index.html")


@api.route('/game', methods=['GET'])
def game():
    return render_template("admin/game/index.html")


@api.route('/user', methods=['GET'])
def user():
    return render_template("admin/user/index.html")


@api.route('/blog', methods=['GET'])
def blog():
    return render_template("admin/blog/index.html")


@api.route('/login', methods=['GET'])
def login():
    return render_template("admin/login.html")


@api.route('/user/list', methods=['GET'])
def user_list():
    return render_template("admin/user/list.html")


@api.route('/user/add', methods=['GET'])
def user_add():
    return render_template("admin/user/add.html")


@api.route('/user/detail/<user_id>', methods=['GET'])
def user_detail(user_id):
    return render_template("admin/user/detail.html", user_id=user_id)


@api.route('/user/edit/<user_id>', methods=['GET'])
def user_edit(user_id):
    return render_template("admin/user/edit.html", user_id=user_id)


@api.route('/blog/article/list', methods=['GET'])
def article_list():
    return render_template("admin/blog/list.html")


@api.route('/blog/article/add', methods=['GET'])
def article_add():
    return render_template("admin/blog/add.html")


@api.route('/blog/article/detail/<article_id>', methods=['GET'])
def article_detail(article_id):
    return render_template("admin/blog/detail.html", article_id=article_id)


@api.route('/blog/article/edit/<article_id>', methods=['GET'])
def article_edit(article_id):
    return render_template("admin/blog/edit.html", article_id=article_id)
