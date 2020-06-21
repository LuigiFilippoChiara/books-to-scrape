# -*- coding: utf-8 -*-
import scrapy
from book_data_item.items import BookDataItem

# this is a slightly more advanced spider
# Instead of simply yielding a dictiornary, the BookPriceItem is implemented,
# instantiated and returned

class BookDataItemSpider(scrapy.Spider):
    name = 'book_data_item_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com//']
    count = 0

    def parse(self, response):
        self.log(f"I just visited {response.url}")

        for article in response.css("article.product_pod"):

            item = BookDataItem()
            # way we refer to a static class attribute
            BookDataItemSpider.count += 1

            item["item_number"] = BookDataItemSpider.count
            item["title"] = article.css("h3 > a::attr(title)").get()
            item["price"] = article.css("p.price_color::text").get()
            item["stars"] = article.css("p::attr(class)").get().split(" ")[-1]
            item["thumbnail_path"] = article.css("div > a > img::attr(src)").get()
            item["detail_book_url"] = article.css("div > a::attr(href)").get()

            yield item

        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)
