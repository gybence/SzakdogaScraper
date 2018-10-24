import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class SzakdolgozatSpider(scrapy.Spider):
	name = 'szakdolgozat_spider'
	# allowed_domains = []
	
	def __init__(self, url='', *args, **kwargs):
		super(SzakdolgozatSpider, self).__init__(*args, **kwargs)
		self.start_urls.append(url)
		
	
	def parse(self, response):
	
		title = response.xpath('//title/text()').extract_first()
		content_title = response.xpath('//div/h1/span/text()').extract_first()
		date = response.xpath('//div[@class="datum"]/text()').extract_first().strip()
		author = response.xpath('//div[contains(@class,"szerzo")]/div[contains(@class,"kovetes")]/a/text()').extract_first()
		
		related_titles = response.xpath('//div[@class="related_box__item"]')
		related_titles_list = []
		for t in related_titles:
			rel_title = t.xpath('.//a/text()').extract_first()
			rel_desc = t.xpath('.//div/text()').extract_first()
			rel_href = t.xpath('.//a').xpath('@href').extract_first()
			item = {'rel_title': rel_title, 'rel_desc': rel_desc, 'rel_href': rel_href}
			related_titles_list.append(item)
		
		lead = response.xpath('//div[@class="lead_container"]/div[@class="lead"]/text()').extract_first()
		lead_text = None
		if lead is not None:
			lead_text = lead.strip()
		else:
			lead_text = ""
		
		article_children = response.xpath('//div[@class="cikk-torzs"]/*[not((name()="div" or name()="aside") and not(contains(@class,"eyecatcher")))]')
		article_children_list = []
		for a in article_children:
			tipus = a.xpath("name()").extract_first()
			parts = None
			parts_concat = None
			if tipus == "p":
				parts = a.xpath(".//text()").extract()	
				parts_concat = ''.join(parts).strip()
			elif tipus == "blockquote":
				parts = a.xpath('.//p/text()').extract()
				parts_concat = ''.join(parts).strip()
			elif tipus == "div":
				parts_concat = a.xpath('.//div/p/text()').extract_first().strip()
			elif tipus == "ul":
				parts = a.xpath('./li/text()').extract()
				parts_concat = ''.join(parts).strip()
			article_children_list.append(parts_concat)			
		
		yield {'content_title': content_title, 'title': title, 'author': author, 'date': date, 'related_titles': related_titles_list, 'lead': lead_text, 'article_children': article_children_list}	