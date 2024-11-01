#!/bin/bash

scrapy runspider book_images_thumbnails/spiders/book_images_thumbnails_spider.py -O books.json
scrapy runspider book_images_thumbnails/spiders/book_images_thumbnails_spider.py -O books.csv