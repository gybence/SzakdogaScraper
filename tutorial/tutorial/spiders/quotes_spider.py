import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class QuotesSpiderSpider(scrapy.Spider):
	name = 'quotes_spider'
	# allowed_domains = []
	
	def __init__(self, url='', *args, **kwargs):
		super(QuotesSpiderSpider, self).__init__(*args, **kwargs)
		self.start_urls.append(url)
		
	
	def parse(self, response):
	
		title = response.xpath('//title/text()').extract_first()
		content_title = response.xpath('//div/h1/span/text()').extract_first()
		date = response.xpath('//div[@class="datum"]/text()').extract_first().strip()
		author = response.xpath('//div[@class="szerzo "]/div[@class="kovetes"]/a[@rel="author"]/text()').extract_first()
		
		related_titles = response.xpath('//div[@class="related_box__item"]')
		related_titles_list = []
		for t in related_titles:
			rel_title = t.xpath('.//a/text()').extract_first()
			rel_desc = t.xpath('.//div/text()').extract_first()
			rel_href = t.xpath('.//a').xpath('@href').extract_first()
			item = {'rel_title': rel_title, 'rel_desc': rel_desc, 'rel_href': rel_href}
			related_titles_list.append(item)
		
		lead = response.xpath('//div[@class="lead_container"]/div[@class="lead"]/text()').extract_first().strip()
		
		article_children = response.xpath('//div[@class="cikk-torzs"]/*[not(contains(@class,"goAdverticum ad-label") or contains(@id, "microsite_microsite"))]')
		article_children_list = []
		for a in article_children:
			type = a.xpath("name()").extract_first()
			if type == "p":
				par = a.xpath(".//text()").extract_first().strip()
				item = {'par': par}
				article_children_list.append(item)
			
		
		yield {'content_title': content_title}
		yield {'title': title}	
		yield {'date': date}
		yield {'related_titles': related_titles_list}
		yield {'lead': lead}
		yield {'article_children': article_children_list}
		