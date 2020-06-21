# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookDataItem(scrapy.Item):
    item_number = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    stars = scrapy.Field()
    thumbnail_path = scrapy.Field()
    detailed_book_url = scrapy.Field()
