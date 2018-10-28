from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.settings import Settings
from szakdolgozat_project.szakdolgozat.spiders.index_spider import IndexSpider
import time
import os
import multiprocessing as mp

allowed_urls = ['https://index.hu/']

class SzakdolgozatCrawler(object):

	def crawl(self, spider,arg):
		crawled_items = []

		def add_item(item):
			crawled_items.append(item)

		process = CrawlerProcess()
		
		settings = Settings()
		os.environ['SCRAPY_SETTINGS_MODULE'] = 'szakdolgozat_project.szakdolgozat.settings'
		settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
		settings.setmodule(settings_module_path, priority = 'project')

		crawler = Crawler(spider, settings)
		crawler.signals.connect(add_item, signals.item_scraped)
		process.crawl(crawler, url = arg)

		process.start()

		return crawled_items
		
def _crawl(queue,arg):
	crawler = SzakdolgozatCrawler()
	spiderObj = IndexSpider()
	res = crawler.crawl(spiderObj,arg)
	queue.put(res)

def crawl(arg):
	if validate_url(arg) is False:
		return None
	q = mp.Queue()
	p = mp.Process(target = _crawl, args = (q,arg,))
	p.start()
	res = q.get()
	p.join()
	return res
	
def validate_url(arg):
	for url in allowed_urls:
		if url in arg:
			return True
	return False