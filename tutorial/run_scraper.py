# from tutorial.tutorial.spiders.quotes_spider import QuotesSpiderSpider
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# import os
# import time
# import sys


# class Scraper:
	# def __init__(self):
		# settings_file_path = 'tutorial.tutorial.settings' # The path seen from root, ie. from main.py
		# os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
		# self.process = CrawlerProcess(get_project_settings())
		# self.spiders = QuotesSpiderSpider # The spider you want to crawl

	# def run_spiders(self,arg):
		# self.process.crawl(self.spiders)
		# self.process.start()  # the script will block here until the crawling is finished
		# time.sleep(0.5) #ez ujrainditja az egeszet lol
		# os.execl(sys.executable, sys.executable, *sys.argv)

from scrapy.crawler import CrawlerRunner
import scrapy
from crochet import setup
from importlib import import_module
setup()

def run_spider(arg, arg2):
	settings = Settings()
	os.environ['SCRAPY_SETTINGS_MODULE'] = 'scrapy.tutorial.settings'
	settings_module_path = os.environ['SCRAPY_SETTINGS_MODULE']
	settings.setmodule(settings_module_path, priority='project')
	
	module_name="tutorial.tutorial.spiders.{}".format(arg)
	scrapy_var = import_module(module_name)   #do some dynamic import of selected spider   
	spiderObj=scrapy_var.QuotesSpiderSpider()		   #get mySpider-object from spider module
	
	crawler = CrawlerRunner(settings)   #from Scrapy docs
	spiderObj.setthings(arg2)
	d = crawler.crawl(spiderObj)