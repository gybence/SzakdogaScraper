from . import normalize
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class ASpider(scrapy.Spider):
	name = 'cnn_spider'
	
	def __init__(self, url='', *args, **kwargs):
		super(ASpider, self).__init__(*args, **kwargs)
		self.start_urls.append(url)
		
	
	def parse(self, response):
		title = response.xpath('//title/text()').extract_first()
		content_title = response.xpath('//div/h1/span/text()').extract_first()
			
		
		yield {'Url': self.start_urls[0], 'ContentTitle': content_title, 'Title': title}