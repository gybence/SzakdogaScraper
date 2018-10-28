from flask import Flask, request, jsonify, abort
import json
from szakdolgozat_project.szakdolgozat_crawler import crawl
app = Flask(__name__)

@app.route('/scrape', methods=['GET', 'POST'])
def scrape_POST():
	print("==============================================================================================================")
	content = request.json
	print('URL: %s' %content['url'])
	scraped_json = crawl(content["url"])
	
	if scraped_json is None:
		abort(404)
	
	print("==============================================================================================================")	
	return (json.dumps(scraped_json[0])).encode("utf-8")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)