#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2016/9/18
import itertools
import json
import string

from scrapy import Request
from scrapy.spiders import Spider

from DomainNameSearch.items import DomainnamesearchItem


class XinNetSpider(Spider):
    name = 'xinnet'
    start_urls = [
        'http://checkdomain.xinnet.com/domainCheck?searchRandom=0&prefix=yaochao&suffix=.vip'
    ]

    suffixs = ['.com', '.net', '.cn', '.shop', '.xyz', '.vip', '.cc', '.top', '.me', '.win',
               '.pub', '.site', '.wang', '.bid', '.pw', '.com.cn', '.net', '.space', '.link', '.online',
               '.tech', '.click', '.news', '.ltd', '.loan', '.date', '.trade', '.party', '.download', '.asia',
               '.website', '.red', '.blue', '.pink', '.poker', '.pro', '.rocks', '.video', '.photo', '.pics',
               '.sexy', '.audio', '.market', '.biz', '.la', '.mobi', '.co', '.so', '.info',
               '.hk', '.tv', '.hiphop', '.live', '.flowers', '.hosting', '.tips', '.lol', '.wiki', '.ink', '.design',
               '.farm', '.care', '.camp', '.fail', '.mom', '.shoes', '.guide', '.solar', '.cheap', '.zone', '.land',
               '.cab', '.cash', '.toys', '.town', '.fish', '.house', '.media', '.tools', '.watch', '.lawyer', '.guru',
               '.tax', '.limo', '.fund', '.green', '.host', '.org', '.gov.cn', '.net.cn', '.org.cn', '.ac.cn', '.name',
               '.tm', '.ren', '.club', '.cool', '.company', '.city', '.email', '.software',
               '.ninja', '.bike', '.today', '.life'
               ]  # , '.网址', '.集团', '.中国', '.公司', '.网络', '.在线', '.中文网', '.移动', '.网店', '.我爱你'

    def start_requests(self):
        search_url = 'http://checkdomain.xinnet.com/domainCheck?searchRandom=0'
        prefixs = self.random_domain(2)  # 随机生成字母数字组合的位数
        print len(prefixs)
        for prefix in prefixs:
            for suffix in self.suffixs:
                item = DomainnamesearchItem()
                item['prefix'] = prefix
                item['suffix'] = suffix
                item['_id'] = prefix + suffix
                url = search_url + '&prefix=' + prefix + '&suffix=' + suffix
                item['url'] = url
                request = Request(url=url, callback=self.parse)
                request.meta['item'] = item
                yield request

    def parse(self, response):
        item = response.meta['item']
        result = json.loads(response.body[5:][:-1])[0]['result'][0]['yes']
        if result:
            item['yes'] = True
            item['price'] = result[0]['price']
        else:
            item['yes'] = False
        yield item

    def random_domain(self, length=1):
        '''
        只是length长度的全排列
        :param length: 指定长度
        :return: domains
        '''
        domains = []
        elements = string.ascii_lowercase + ''.join([str(i) for i in xrange(10)])
        for j in itertools.permutations(elements, length):
            domains.append(''.join(j))
        if length != 1:
            for k in elements:
                domains.append(k * length)
        return domains

    def random_domain_all(self, maxlength=1):
        '''
        包括1-maxlenth所有位数的全排列
        :param maxlength: 最大长度
        :return: domains
        '''
        domains = []
        elements = string.ascii_lowercase + ''.join([str(i) for i in xrange(10)])
        for i in xrange(maxlength):
            i = i + 1
            for j in itertools.permutations(elements, i):
                domains.append(''.join(j))
            if i != 1:
                for k in elements:
                    domains.append(k * i)
        return domains
