from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from szakdolgozat_project.szakdolgozat_crawler import crawl

hostName = ""

class WebServer(BaseHTTPRequestHandler):
	def _set_json_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_HEAD(self):
		self._set_headers()

	def do_GET(self):
		self._set_headers()
		self.wfile.write(b"<html><body><h1>Szakdolgozat Scraper Webserver!</h1></body></html>")
		
	def do_POST(self):
		print("==============================================================================================================")
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)

		url_obj = json.loads(post_data) 
		print('Received URL for scraping: %s' %url_obj["url"])
		
		scraped_json = crawl(url_obj["url"])
		self._set_json_headers()
		self.wfile.write((json.dumps(scraped_json)).encode("utf-8"))
		print("==============================================================================================================")
						
def run(server_class=HTTPServer, handler_class=WebServer, port=8080):
	server_address = (hostName, port)
	httpd = server_class(server_address, handler_class)
	print ('Serving on port: %s' %port)
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	print ('Starting httpd...')
	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()