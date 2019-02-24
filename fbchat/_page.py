# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import attr
from typing import Optional
from ._thread import ThreadType, Thread


@attr.s(cmp=False, init=False)
class Page(Thread):
    """Represents a Facebook page. Inherits `Thread`"""

    #: The page's custom url
    url = attr.ib(None, type=Optional[str])
    #: The name of the page's location city
    city = attr.ib(None, type=Optional[str])
    #: Amount of likes the page has
    likes = attr.ib(None, type=Optional[int])
    #: Some extra information about the page
    sub_title = attr.ib(None, type=Optional[str])
    #: The page's category
    category = attr.ib(None, type=Optional[str])

    def __init__(
        self,
        uid,
        url=None,
        city=None,
        likes=None,
        sub_title=None,
        category=None,
        **kwargs
    ):
        super(Page, self).__init__(ThreadType.PAGE, uid, **kwargs)
        self.url = url
        self.city = city
        self.likes = likes
        self.sub_title = sub_title
        self.category = category
