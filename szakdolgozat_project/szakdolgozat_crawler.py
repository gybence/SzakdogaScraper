from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.settings import Settings
from szakdolgozat_project.szakdolgozat.spiders.szakdolgozat_spider import SzakdolgozatSpider
import time
import os
import multiprocessing as mp

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
	spiderObj = SzakdolgozatSpider()
	res = crawler.crawl(spiderObj,arg)
	queue.put(res)

def crawl(arg):
	q = mp.Queue()
	p = mp.Process(target = _crawl, args = (q,arg,))
	p.start()
	res = q.get()
	p.join()
	return res