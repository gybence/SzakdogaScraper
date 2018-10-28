import requests

ENDPOINT = "http://localhost:5000/scrape"
# value = input("URL to scrape: ")
value ="https://xindex.hu/sport/forma1/2018/10/13/briatore_ravilagitott_miert_bukik_vettel_iden"

data = {"url":value}
r = requests.post(url = ENDPOINT, json = data)
res = r.text
print("%s"%res)