# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from book_data_item_loader.items import BookDataItemLoaderItem

# This is a slightly more complex spider.
# Here data is loaded into the BookDataItemLoaderItem with an ItemLoader.
# This syntax is more complex but allows more flexibility, for
# example we can create an item taking data from multiple web pages.


class BookDataItemLoaderSpider(scrapy.Spider):
    name = 'book_data_item_loader_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com//']
    count = 0

    def parse(self, response):
        self.log(f"I just visited {response.url}")

        for article in response.css("article.product_pod"):

            # item loader initialization
            item_loader = ItemLoader(item=BookDataItemLoaderItem(), selector=article)
            BookDataItemLoaderSpider.count += 1

            item_loader.add_value('item_number', BookDataItemLoaderSpider.count)
            item_loader.add_css('title', "h3 > a::attr(title)")
            item_loader.add_css('price', "p.price_color::text")
            item_loader.add_css('stars', "article > p::attr(class)")
            item_loader.add_css('thumbnail_path', "div > a > img::attr(src)")
            item_loader.add_css('detailed_book_url', "div > a::attr(href)")

            # crawl detailed book page
            detailed_book_url = article.css("div > a::attr(href)").get()
            if detailed_book_url:
                # parse the detailed book page with an approprate parse method
                yield response.follow(
                    url=detailed_book_url,
                    callback=self.parse_detailed_book_url,
                    # send some meta data to the parse_detailed_book_url method
                    meta={'item': item_loader.load_item()},
                    dont_filter=True
                    )
            else:
                yield item_loader.load_item()

        # move to following pages
        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)


    # callback method for scraping detailed book page
    # it adds other fields to the item_loader object, which is passed as meta data
    def parse_detailed_book_url(self, response):
        self.log(f"I just visited {response.url}")

        item_loader_next = ItemLoader(item=response.meta['item'], response=response)
        item_loader_next.add_css('image_url', "div.carousel-inner > div > img::attr(src)")
        item_loader_next.add_css('product_description', "div#product_description + p::text")

        return item_loader_next.load_item()

















