# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from book_images_thumbnails.items import BookImagesThumbnailsItem

# This spider downloas both text data and images.
# The images are downloaded following the thumbnail path of the main
# page of the website. At every run, they are downloaded automatically in the
# directory <IMAGES_STORE>/full specified in settings.py.
# In addition, the pipeline automatically creates thumbnails of the 
# downloaded images, as specified in settings.py.
# In this example we are creating thumbnails of already
# small pictures (they were already thumbnails to begin with).
# Moreover, full is a sub-directory to separate full images from created 
# thumbnails (if used).


class BookImagesThumbnailsSpider(scrapy.Spider):
    name = 'book_images_thumbnails_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']
    count = 0
    # Optional: we can limit the extraction of media from links
    # that follow some rules in this way (.* is RegEx)
    rules = [Rule(LinkExtractor(allow=['/media/.*']), callback='parse')]

    def parse(self, response):
        self.log(f"I just visited {response.url}")

        for article in response.css("article.product_pod"):
            BookImagesThumbnailsSpider.count += 1

            image = BookImagesThumbnailsItem()
            image["item_number"] = BookImagesThumbnailsSpider.count
            image["title"] = article.css("h3 > a::attr(title)").get()
            image["price"] = article.css("p.price_color::text").get()

            relative_image_url = article.css("div > a > img::attr(src)").get()
            absolute_image_url = response.urljoin(relative_image_url)
            image["image_urls"] = [absolute_image_url]

            yield image

        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
        	yield response.follow(url=next_page_url, callback=self.parse)
