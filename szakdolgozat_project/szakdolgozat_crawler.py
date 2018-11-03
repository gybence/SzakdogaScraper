from szakdolgozat_project.postgres_szakdolgozat import get_for_validation
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.settings import Settings
from scrapy import signals
from importlib import import_module
import multiprocessing as mp
import time
import os

class SzakdolgozatCrawler(object):

	def crawl(self, spider, arg):
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
		
def _crawl(queue, name, arg):
	try:
		module_name= 'szakdolgozat_project.szakdolgozat.spiders.{}'.format(name)
		scrapy_var = import_module(module_name)
		spiderObj = scrapy_var.ASpider()	
		
		crawler = SzakdolgozatCrawler()
		res = crawler.crawl(spiderObj,arg)
		queue.put(res)
	except (ModuleNotFoundError):
		queue.put(None)

def crawl(pgpw, name, arg):	
	q = mp.Queue()
	p = mp.Process(target = _crawl, args = (q, name, arg, ))
	p.start()
	res = q.get()
	p.join()
	return res
	
