# -*- coding: utf-8 -*-
import scrapy

class QuotesSpiderSpider(scrapy.Spider):
	name = 'quotes_spider'
	# allowed_domains = ['quotes.toscrape.com']
	# 'http://quotes.toscrape.com/'
	start_urls = []
	def init(self,arg):
		print(arg)
		self.start_urls.append(arg)
	
	def parse(self, response):
		quotes = response.xpath("//div[@class='quote']")
		for quote in quotes:
			text = quote.xpath(".//span[@class='text']/text()").extract_first()
			author = quote.xpath(".//small//text()").extract_first()
			yield {'quote': text, "author": author}
	
	
		# quotes = response.xpath("//div[@class='quote']//span[@class='text']/text()").extract()
		# yield {'quotes': quotes}