import requests
from config import API_KEY

def fetch_stock_data(symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "datatype": "json"
    }
    response = requests.get(base_url, params=params)
    return response.json()
