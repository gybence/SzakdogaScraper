from flask import Flask, request, jsonify
import json
from szakdolgozat_project.szakdolgozat_crawler import crawl
app = Flask(__name__)

@app.route('/scrape', methods=['GET', 'POST'])
def scrape_POST():
	print("==============================================================================================================")
	content = request.json
	
	print('Received URL for scraping: %s' %content['url'])
	scraped_json = crawl(content["url"])
	print(type(scraped_json[0]))
	print("==============================================================================================================")	
	return (json.dumps(scraped_json)).encode("utf-8")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)