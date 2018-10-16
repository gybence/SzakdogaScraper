import requests

API_ENDPOINT = "http://localhost:8080"
# value = input("URL to scrape: ")
value ="https://index.hu/sport/forma1/2018/10/13/briatore_ravilagitott_miert_bukik_vettel_iden"

data = {"url":value}
r = requests.post(url = API_ENDPOINT, json = data)
res = r.text
print("%s"%res)