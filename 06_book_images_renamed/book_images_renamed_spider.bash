#!/bin/bash

scrapy runspider book_images_renamed/spiders/book_images_renamed_spider.py -O books.json
scrapy runspider book_images_renamed/spiders/book_images_renamed_spider.py -O books.csv