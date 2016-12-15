# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...helpers.utils import require_value_from_dict


class Article(Base0):
    """
    文章
    """

    def __init__(self, obj):
        Base0.__init__(self)

        self.slug = require_value_from_dict(obj, 'slug')  # 文章唯一标识, 用作url

        self.title = require_value_from_dict(obj, 'title')
        self.content = require_value_from_dict(obj, 'content')
        self.summary = require_value_from_dict(obj, 'summary')  # 摘要

        # self.user_id = require_value_from_dict(obj, 'user_id')
        self.author = require_value_from_dict(obj, 'author')

        self.date = time.time()  # 创建时间
        self.modified = time.time()  # 修改时间

        self.category = require_value_from_dict(obj, 'category')
        self.tags = require_value_from_dict(obj, 'tags')

        self.status = 0  # -1: 删除, 0: 草稿, 1:发布

        self.view_times = 0  # 访问次数
