#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from tutorial.custom_crawler import crawl

hostName = ""
hostPort = 8080
# scraper = Scraper()
class S(BaseHTTPRequestHandler):
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
		self.wfile.write("got".encode("utf-8"))
		
	def do_POST(self):
		print("==============================================================================================================")
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		returned_data = self.csinald(post_data)
		vmi = self.scrapyzz(returned_data["returl"])

		self._set_json_headers()

		self.wfile.write((json.dumps(vmi)).encode("utf-8"))
		
	def scrapyzz(self, arg):
		vmi = crawl(arg)
		return vmi
		
	def csinald(self, post_data):
		obj = json.loads(post_data)
		asd = obj["url"]
		data = {"returl":asd}
		return data
		
def run(server_class=HTTPServer, handler_class=S):
	server_address = (hostName, hostPort)
	httpd = server_class(server_address, handler_class)
	print ('Starting httpd... %s' % hostPort)
	httpd.serve_forever()

if __name__ == "__main__":
	from sys import argv

	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run()