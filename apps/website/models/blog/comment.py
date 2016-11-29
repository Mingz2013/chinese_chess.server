# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from ..base0 import Base0
from ...utils.utils import require_value_from_dict


class Comment(Base0):
    """
    文章评论
    """

    def __init__(self, title):
        Base0.__init__(self)

        self.title = title
        self.status = 0  # -1: 删除, 0: 草稿, 1:发布
        self.article_count = 0  # 文章数量
        self.date = time.time()
        self.modified = time.time()
        pass
