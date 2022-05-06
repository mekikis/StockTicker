import pandas as pd
from yahoofinancials import YahooFinancials
import datetime
import paho.mqtt.client as paho

broker = "192.168.2.100"
port = 1883

today = datetime.date.today()
todayY = today.strftime("%Y-%m-%d")
week_ago = today - datetime.timedelta(days=7)
week_agoY = week_ago.strftime("%Y-%m-%d")

cryptocurrencies = ['BTC-EUR']
# stocks = ['AAPL', 'V']
stocks = ["AAPL", "AMD", "AMZN", "APPS", "ATIV", "BAC", "DIS", "GOOG", "HITIF", "KO", "MSFT", "NIO", "NVDA", "PG", "PLTR", "PYPL", "SPOT", "T", "TSLA", "V", "VZ", "WMT"]
etfs = ["VWRL.AS", "VUSA.AS", "EQQQ.PA"]

yahoo_financials_stocks = YahooFinancials(stocks)
yahoo_financials_cryptocurrencies = YahooFinancials(cryptocurrencies)
seven_days_crypto_prices = yahoo_financials_cryptocurrencies.get_historical_price_data(start_date=week_agoY, end_date=todayY, time_interval='daily')
current_crypto_prices = yahoo_financials_cryptocurrencies.get_current_price()
seven_days_crypto_prices_df = pd.DataFrame(seven_days_crypto_prices['BTC-EUR']['prices']).mean()
seven_days_btc = (seven_days_crypto_prices_df.high+seven_days_crypto_prices_df.low)/2
print("Current price: ", current_crypto_prices['BTC-EUR'], "  7-days average: ", seven_days_btc)
print("Sell target: ", 1.1*seven_days_btc, "  Buy target: ", 0.9*seven_days_btc)
print(yahoo_financials_stocks.get_current_price())
def on_publish(client, userdata, result):
    print("ok")
    pass

# crypto_tracker = paho.Client("btc")
# crypto_tracker.on_publish = on_publish
# crypto_tracker.connect(broker, port)

if (current_crypto_prices['BTC-EUR'] > 1.1*seven_days_btc):
    # ret = crypto_tracker.publish("crypto/btc", "SELL")
    print("sell ok")
elif (current_crypto_prices['BTC-EUR'] < 0.9*seven_days_btc):
    # ret = crypto_tracker.publish("crypto/btc", "BUY")
    print("buy ok")
else:
    # ret = crypto_tracker.publish("crypto/btc", "NOTHING")
    print("do nothing")
