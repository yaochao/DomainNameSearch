#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2016/8/11

import random
from DomainNameSearch.misc.useragents import USER_AGENTS


# DownloadMiddleware
class UserAgentMiddleware(object):
    # 每当有request时,会自动调用此方法
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers['User-Agent'] = user_agent
