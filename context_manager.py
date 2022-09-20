"""
1. Pass exchange rate currency type
2. Connects to api and get data
3. 
"""
from urllib import response
import requests, json

class ExchangeRate:
    def __init__(self, currency):
        self.currency = currency
        self.json_file = open('currency.json', 'w+')

    def get_exchange_rate(self):
        response = requests.get(
            url ="https://api.exchangerate.host/latest?base=USD"
        )
        exchange_rate = response.json()
        try:
            return exchange_rate.get('rate')
        except:
            return {}
    def __enter__(self):
        exchange_rate = self.get_exchange_rate()
        json.dump(exchange_rate, self.json_file, indent=4)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.json_file.close()

with ExchangeRate('USD') as exchange_rate:
    currency_type = input('Currency Type: ')
    amount = input('Amount: ')
    exchange_value = exchange_rate.get(currency_type, 1)
    print('Converted Value: ', exchange_value)