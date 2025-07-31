import time
import ccxt

api_key = 'your_api_key'
api_secret = 'your_api_secret'

exchange = ccxt.mexc({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True,
})

while True:
    balance = exchange.fetch_balance()
    print(balance)
    time.sleep(10)
