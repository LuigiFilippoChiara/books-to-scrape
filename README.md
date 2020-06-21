# Books to scrapy
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](/LICENSE)

Learning how to use scrapy to download text data and images from the web.

## Project description

We will use [scrapy](https://scrapy.org) to download text data and images from [books.toscrape.com](http://books.toscrape.com), a demo website built for web scraping purposes, which contains data about 1000 books.

This repository is divided into six indipendent directories: one self-contained scrapy spider and five scrapy projects.

2. `01_simple_spider` contains a self-contained spider. When lanched, it downloads book data (*title* and *price*) and crawls multiple web pages automatically.

2. `02_book_data_dict` is the simplest possible scrapy project. It downloads book data (*item number, title, price* and *star rating*) yielding a simple Python dictionary.

3. `03_book_data_item` downloads some book data (*item number, title, price, star rating, thumbnail path* and *detailed book url*), but it yields a **scrapy item** instead of a simple dictionary. Moreover the **start_requests** initialization method is used instead of the simpler **start_urls** attribute.

4. `04_book_data_item_loader` uses a **scrapy item loader** object to load the book data item. This syntax is more complex, but allows more flexibility. For example we can create an item taking data from multiple web pages. For example here we download *item number, title, price, star rating, thumbnail path, detailed book url, image_url* and *product description* for each book. In order to scrape the detailed book page, a secondary parse method has to be defined.

5. `05_book_images_thumbnails` downloads both text data and images. Here the images are downloaded following the thumbnail path of the main page of the website. This project is slightly more complex as it has to use a scrapy item with predefined attributes together with the default **scrapy image pipeline**, which needs to be activated in `setting.py`. Thanks to the pipeline images are automatically downloaded inside the `images/full` directory, and named with a SHA1 hash of their urls (by default). In addition, the pipeline automatically creates thumbnails of the 
downloaded images in `images/thumb`, as specified in `settings.py`. In this example we are creating thumbnails of already small pictures (they were already thumbnails to begin with).

6. `06_book_images_renamed` is similar to the previous one, but these time we want to rename the downloaded images. In order to do this we need to create a **custom scrapy pipeline** that inherits from the default image pipeline. This time the images are downloaded from the detailed book page, so they have higher resolution. At every run, they are downloaded automatically in the directory `images/full`. Moreover, thanks to the custom pipeline, the image names are changed from the default hash to the actual book title.


## Getting started

Library you need: scarpy, pillow



## A few notes about scrapy commands

Scrapy comes in with a few very usefull command line commands. To have a look at a list of these commands, simply run the command

```
$ scrapy
```

once the program is correctly installed. Every scrapy commands starts with the `scrapy` keyword. Most of the time you have to be in the project root directory (the one with scrapy.cfg configuration file) to run these commands correctly.

#### 1. Create a new scrapy project

```
$ scrapy startproject <project_name>
``` 

#### 2. Create a new spider inside a project

```
$ scrapy genspider <spider_name> <url_domain>
``` 

#### 3. List of spiders in a project

```
$ scrapy list
``` 

#### 4. Run a self-contained spider

```
$ scrapy runspider <spider_script.py> 
``` 

The spider will run with the implemented logic. By default the crawled data will be printed to screen, but you can also specify an optional `--output filename.format` (for example `-o out.csv`) argument to save it to a file with the requested format. Scrapy automatically implement some output formats, such as `csv`, `json`, `jsonlines`, `xml` and `pickle`.

#### 5. Run a spider inside a project

```
$ scrapy crawl <spider_name>
``` 
Again, you can save the data with the `--output filename.format` optional argument.

## License

This project is licensed under the MIT License. Use it as you wish.