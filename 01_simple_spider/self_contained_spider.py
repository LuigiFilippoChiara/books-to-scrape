# -*- coding: utf-8 -*-
import scrapy

# The simplest possible scrapy program.


class BookSpider(scrapy.Spider):
	name = 'bookspider'
	start_urls = ["http://books.toscrape.com"]

	def parse(self, response):
		self.log(f"I just visited {response.url}")

		for article in response.css('article.product_pod'):
			yield {
				'title': article.css("h3 > a::attr(title)").extract_first(),
				'price': article.css(".price_color::text").extract_first()
			}

		next_page_url = response.css("li.next > a::attr(href)").get()
		if next_page_url:
			yield response.follow(url=next_page_url, callback=self.parse)
