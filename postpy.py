import requests

API_ENDPOINT = "http://localhost:8080"

	# http://quotes.toscrape.com/
	# file:///C:/Users/Bence/Desktop/quotes.html
# value = input("URL to scrape: ")
# value="file:///C:/Users/Bence/Desktop/index.html"
# value="file:///C:/Users/Bence/Desktop/quotes.html"
value ="https://index.hu/sport/forma1/2018/10/13/briatore_ravilagitott_miert_bukik_vettel_iden"

data = {"url":value}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, json = data)

# extracting response text
res = r.text
print("Response: %s"%res)