#!/bin/bash

scrapy runspider book_data_item/spiders/book_data_item_spider.py -O books.json
scrapy runspider book_data_item/spiders/book_data_item_spider.py -O books.csv