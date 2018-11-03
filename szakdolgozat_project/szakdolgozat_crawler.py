from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.settings import Settings
import time
from importlib import import_module
import os
import multiprocessing as mp
from szakdolgozat_project.postgre_szakdolgozat import get_for_validation

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
	module_name= 'szakdolgozat_project.szakdolgozat.spiders.{}'.format(name)
	scrapy_var = import_module(module_name)
	spiderObj = scrapy_var.ASpider()	
	
	crawler = SzakdolgozatCrawler()
	res = crawler.crawl(spiderObj,arg)
	queue.put(res)

def crawl(pgpw, arg):
	name = get_for_validation(pgpw, arg)
	if name is None:
		return None
		
	q = mp.Queue()
	p = mp.Process(target = _crawl, args = (q, name[0], arg, ))
	p.start()
	res = q.get()
	p.join()
	return res
	
