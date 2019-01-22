# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join

def remove_quotations(value):
    return value.replace(u"\u2019", '').replace(u"\u2013", '').replace(u"\u00a0", '').replace(u"\u00a3", '')

def remove_skipspace(value):
    return value.replace("\n", '')

class ReviewItem(scrapy.Item):
    pass



