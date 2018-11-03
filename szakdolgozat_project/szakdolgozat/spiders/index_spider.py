from . import normalize
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class ASpider(scrapy.Spider):
	name = 'index_spider'
	
	def __init__(self, url='', *args, **kwargs):
		super(ASpider, self).__init__(*args, **kwargs)
		self.start_urls.append(url)
		
	
	def parse(self, response):
		content_title = response.xpath('//title/text()').extract_first()
		title = response.xpath('//div/h1/span/text()').extract_first()
		date = response.xpath('//div[@class="datum"]/text()').extract_first()
		date_text = None
		if date is not None:
			date_text = date.strip()
		author = response.xpath('//div[contains(@class,"szerzo")]/div[contains(@class,"kovetes")]/a/text()').extract_first()
		
		related_titles = response.xpath('//div[@class="related_box__item"]')
		related_titles_list = []
		for t in related_titles:
			rel_title = t.xpath('.//a/text()').extract_first()
			rel_desc = t.xpath('.//div/text()').extract_first()
			rel_href = t.xpath('.//a').xpath('@href').extract_first()
			item = {'RelTitle': rel_title, 'RelDesc': rel_desc, 'RelHref': rel_href}
			related_titles_list.append(item)
		
		lead = response.xpath('//div[@class="lead_container"]/div[@class="lead"]/text()').extract_first()
		lead_text = None
		if lead is not None:
			lead_text = normalize(lead)
		
		article_children = response.xpath('//div[@class="cikk-torzs"]/*[not((name()="div" or name()="aside") and not(contains(@class,"eyecatcher")))]')
		article_children_list = []
		for a in article_children:
			tipus = a.xpath('name()').extract_first()
			parts = None
			parts_concat = None
			if tipus == 'p':
				parts = a.xpath('.//text()').extract()
				parts_concat = normalize(''.join(parts))
			elif tipus == 'blockquote':
				parts = a.xpath('.//p/text()').extract()
				parts_concat = ''.join(['\"', normalize(''.join(parts)), '\"'])
			elif tipus == 'div':
				parts_concat = normalize(a.xpath('.//div/p/text()').extract_first())
			elif tipus == 'ul':
				parts = a.xpath('./li/text()').extract()
				for i, p in enumerate(parts): 
					parts[i] = '\u25cf ' + normalize(p)
				parts_concat = '\n\n'.join(parts)
			article_children_list.append(parts_concat)			
		
		yield {'Url': self.start_urls[0], 'ContentTitle': content_title, 'Title': title, 'Author': author, 
		'Date': date_text, 'RelatedTitles': related_titles_list, 'Lead': lead_text, 
		'ArticleChildren': article_children_list}