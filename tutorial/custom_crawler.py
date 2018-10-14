from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.settings import Settings
from tutorial.tutorial.spiders.quotes_spider import QuotesSpiderSpider
import time
import multiprocessing as mp
from scrapy.utils.project import get_project_settings

class CustomCrawler(object):

	def crawl(self, spider,arg):
		crawled_items = []

		def add_item(item):
			crawled_items.append(item)

		process = CrawlerProcess()

		crawler = Crawler(spider, get_project_settings())
		crawler.signals.connect(add_item, signals.item_scraped)
		process.crawl(crawler, url = arg)

		process.start()

		return crawled_items
		
def _crawl(queue,arg):
	crawler = CustomCrawler()
	spiderObj=QuotesSpiderSpider()
	# spiderObj.init(arg)
	res = crawler.crawl(spiderObj,arg)
	queue.put(res)

def crawl(arg):
	q = mp.Queue()
	p = mp.Process(target=_crawl, args=(q,arg,))
	p.start()
	res = q.get()
	p.join()
	return res