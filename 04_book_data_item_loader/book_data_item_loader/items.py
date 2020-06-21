# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


def remove_star_text(input_string):
    """
    Simple preprocess custom method
    """
    if "star-rating" in input_string[0]:
        return input_string[0].split(" ")[-1]
    return input_string


class BookDataItemLoaderItem(scrapy.Item):
    """
    When using ItemLoader we can define an output and input process per field.
    Since ItemLoader returns lists by default, we can take the first element
    of each list -- the data we want -- with the TakeFirst method.
    We also did some processing with the remove_star_text method.
    """
    item_number = scrapy.Field(
        output_processor=TakeFirst())
    title = scrapy.Field(
        output_processor=TakeFirst())
    price = scrapy.Field(
        output_processor=TakeFirst())
    stars = scrapy.Field(
        input_processor=remove_star_text,
        output_processor=TakeFirst())
    thumbnail_path = scrapy.Field(
        output_processor=TakeFirst())
    detailed_book_url = scrapy.Field(
        output_processor=TakeFirst())
    image_url = scrapy.Field(
        output_processor=TakeFirst())
    product_description = scrapy.Field(
        output_processor=TakeFirst())
