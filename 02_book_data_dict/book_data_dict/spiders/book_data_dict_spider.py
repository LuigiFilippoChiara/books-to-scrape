# -*- coding: utf-8 -*-
import scrapy

# this is the simplest spider ever
# It yields a Python dictionary containing the requested data

class BookDataDictSpiderSpider(scrapy.Spider):
    name = 'book_data_dict_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']
    count = 0

    def parse(self, response):
        self.log(f"I just visited {response.url}")

        # ccs selector: all tags <article> that contains class="product_pod"
        for article in response.css("article.product_pod"):

            # way we refer to a static class attribute
            BookDataDictSpiderSpider.count += 1

            yield {
            	"item_number": BookDataDictSpiderSpider.count,
            	"title": article.css("h3 > a::attr(title)").get(),
            	"price": article.css("p.price_color::text").get(),
            	"stars": article.css("p::attr(class)").get().split(" ")[-1],
            	"thumbnail_path": article.css("div > a > img::attr(src)").get(),
            	"detail_book_url": article.css("div > a::attr(href)").get()
            }

        next_page_url = response.css("li.next > a::attr(href)").get()
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)

