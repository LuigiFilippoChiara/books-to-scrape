#!/bin/bash

scrapy runspider book_data_dict/spiders/book_data_dict_spider.py -O books.json
scrapy runspider book_data_dict/spiders/book_data_dict_spider.py -O books.csv