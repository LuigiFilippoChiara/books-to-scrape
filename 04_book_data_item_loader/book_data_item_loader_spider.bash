#!/bin/bash

scrapy runspider book_data_item_loader/spiders/book_data_item_loader_spider.py -O books.json
scrapy runspider book_data_item_loader/spiders/book_data_item_loader_spider.py -O books.csv