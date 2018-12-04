from szakdolgozat_project.postgres_module import get_from_db, insert_to_db, print_delimiter, postgres_authorize, get_for_validation
from szakdolgozat_project.crawler_module import crawl
from flask import Flask, request, jsonify, abort
import datetime
import json
import sys
app = Flask(__name__)

#Packages required: flask, scrapy, psycopg2, requests
@app.route('/scrape', methods=['GET', 'POST'])
def scrape_POST():
	print_delimiter()
	content = request.json
	print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ') + '[flask post] INFO: URL: %s' %content['url'])
	pgpw = app.config.get('pgpw')
	record = get_for_validation(pgpw, content['url'])
	if record is None:
		abort(404)
			
	from_db = get_from_db(pgpw, content['url'])	
	if from_db is not None:
		print_delimiter()
		return from_db
	else: 
		scraped_json = crawl(pgpw, record[2], content['url'])
		if scraped_json is None or len(scraped_json) == 0:
			print_delimiter()
			abort(404)
		else: 
			insert_to_db(pgpw, content['url'], scraped_json[0], record)
			print_delimiter()
			return (json.dumps(scraped_json[0])).encode('utf-8')

if __name__ == '__main__':
	if len(sys.argv) > 1:
		app.config['pgpw'] = sys.argv[1]
		if postgres_authorize(app.config['pgpw']) is True:
			app.run(host='0.0.0.0', port=5000)
		else:
			print("Provide the correct password for the database as the first argument")
	else:
		print("Provide a password for the database as an argument")
