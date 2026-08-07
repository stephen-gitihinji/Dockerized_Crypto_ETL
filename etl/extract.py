import requests as req

def extract_coins():
	#coinpaprika url for obtaining all the coins and their tickers
	url = "https://api.coinpaprika.com/v1/tickers"

	#http request to the url
	response = req.get(url)

	#returning the top 100 coins
	top_100_coins = response.json()[0:100]
	return top_100_coins