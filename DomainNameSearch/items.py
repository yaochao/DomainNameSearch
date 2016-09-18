# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class DomainnamesearchItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    prefix = Field()
    suffix = Field()
    price = Field()
    yes = Field()
    url = Field()
    _id = Field()
