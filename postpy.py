import requests

ENDPOINT = "http://localhost:5000/scrape"
# value = input("URL to scrape: ")
value ="https://edition.cnn.com/2018/11/03/politics/cnn-house-key-races-final-update/index.html"

data = {"url":value}
r = requests.post(url = ENDPOINT, json = data)
res = r.text
print("%s"%res)