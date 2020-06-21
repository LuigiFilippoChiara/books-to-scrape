# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

# Define a custom pipeline that inherits from the default ImagesPipeline.
# We override some default methods.


class BookImagesRenamedPipeline(ImagesPipeline):

	def set_filename(self, response):
		# add RegEx to check if it is a valid filename
		new_name = response.meta['title'].replace("/", "-")
		return f"full/{new_name}.jpg"


	def get_media_requests(self, item, info):
		for image_url in item['image_urls']:
			yield scrapy.Request(image_url, meta={'title': item['title']})


	def get_images(self, response, request, info):
		for key, image, buff in super(BookImagesRenamedPipeline, self).get_images(response, request, info):
			# key is the name of the file in our case
			key = self.set_filename(response)
		yield key, image, buff
