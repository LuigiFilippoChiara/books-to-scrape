# Books to scrapy
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](/LICENSE)

Learning how to use scrapy to download text data and images from the web.

## Project description

In this repo we will use [scrapy](https://scrapy.org) to download text and images from [books.toscrape.com](http://books.toscrape.com). The project is divided into four indipendent scrapy projects:

1. `01_book_data_item` download some book data (item_number, title, price, star rating, thumbnail path and detail book url) yielding a scrapy **item** instead of a simple dictionary.

## A few notes about scrapy

Go in a scrapy project root directory and run some commands with the `scrapy` keyword.  

To see the available spiders in that project type

```
$ scrapy list
``` 

and to run one of them type

```
$ scrapy crawl spider_name -o out.csv
``` 

where `--output filename.format` is an optional argument. Scrapy automatically implement some output formats, such as `csv`, `json`, `jsonlines`, `xml` and `pickle`.  
Additionally you can use the `-L info` option to only print 


## License

This project is licensed under the MIT License. Use it as you wish.