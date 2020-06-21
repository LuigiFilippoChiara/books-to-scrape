# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookImagesRenamedItem(scrapy.Item):
    """
    Item used when downloading images. The 'image_urls' and 'images' fields
    are mandatory if we want to work with the default image pipeline (which is 
    the base class for out custom pipeline).
    Everything related to image downloading is then done automatically 
    under the hood.
    """
    item_number = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()