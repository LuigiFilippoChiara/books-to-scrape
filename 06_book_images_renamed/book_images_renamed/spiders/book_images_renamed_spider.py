# -*- coding: utf-8 -*-
import scrapy
from book_images_renamed.items import BookImagesRenamedItem

# This spider downloas both text data and images.
# The images are downloaded from the detailed book page, so they
# have higher resolution. At every run, they are downloaded automatically in the
# directory <IMAGES_STORE>/full specified in settings.py.
# Moreover, thanks to the custom pipeline, the image names are changed
# from the default hash to the actual book title.


class BookImagesRenamedSpider(scrapy.Spider):
    name = 'book_images_renamed_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']
    count = 0

    def parse(self, response):
        self.log(f"I just visited {response.url}")

        for article in response.css("article.product_pod"):
            BookImagesRenamedSpider.count += 1

            item = BookImagesRenamedItem()
            item["item_number"] = BookImagesRenamedSpider.count
            item["title"] = article.css("h3 > a::attr(title)").get()
            item["price"] = article.css("p.price_color::text").get()

            # crawl detailed book page
            detailed_book_url = article.css("div > a::attr(href)").get()
            if detailed_book_url:
                yield response.follow(
                    url=detailed_book_url,
                    callback=self.parse_detailed_book_page,
                    meta={'item': item},
                    dont_filter=True
                    )
            else:
                yield item

        # logic for following pages
        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
        	yield response.follow(url=next_page_url, callback=self.parse)


    # callback method for scraping detailed book page
    # and downloading images from there
    def parse_detailed_book_page(self, response):
        self.log(f"I just visited {response.url}")

        item = response.meta['item']
        relative_image_url = response.css("div.carousel-inner > div > img::attr(src)").get()
        absolute_image_url = response.urljoin(relative_image_url)
        item["image_urls"] = [absolute_image_url]

        return item

