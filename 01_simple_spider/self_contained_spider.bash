#!/bin/bash

scrapy runspider self_contained_spider.py -O books.json
scrapy runspider self_contained_spider.py -O books.csv