import requests

API_ENDPOINT = "http://localhost:8080"

	# http://quotes.toscrape.com/
	# file:///C:/Users/Bence/Desktop/quotes.html
value = input("URL to scrape: ")

data = {"url":value}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, json = data)

# extracting response text
res = r.text
print("Response: %s"%res)