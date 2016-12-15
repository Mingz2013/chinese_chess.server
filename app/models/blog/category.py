# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...helpers.utils import require_value_from_dict


class Category(Base0):
    """
    文章分类
    """

    def __init__(self, title):
        Base0.__init__(self)

        self.title = title
        self.status = 0  # -1: 删除, 0: 草稿, 1:发布
        self.article_count = 0  # 文章数量
        self.date = time.time()
        self.modified = time.time()
        pass
