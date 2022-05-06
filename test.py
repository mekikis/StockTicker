import pandas as pd
from yahoofinancials import YahooFinancials
import time
import paho.mqtt.client as paho

broker = "192.168.2.100"
port = 1883
print("welcome")
cryptocurrencies = ['BTC-EUR', 'ETH-EUR', 'LTC-EUR', 'XLM-EUR']
# stocks = ["AAPL", "AMD", "AMZN", "APPS", "AZN", "BEP", "DIS", "GOOG", "HITIF", "KO", "MSFT", "NFLX", "NIO", "NVDA", "PG", "PLTR", "PYPL", "SPOT", "T", "TSLA", "V", "VZ", "WMT"]
# etfs = ["VWRL.AS", "VUSA.AS", "EQQQ.PA"]




# yahoo_financials_stocks = YahooFinancials(stocks)

# yahoo_financials_etfs = YahooFinancials(etfs)

while True:
    yahoo_financials_cryptocurrencies = YahooFinancials(cryptocurrencies)
    # current_stock_prices = yahoo_financials_stocks.get_current_price()
    current_crypto_prices = yahoo_financials_cryptocurrencies.get_current_price()
    print(current_crypto_prices)
    # current_etf_prices = yahoo_financials_etfs.get_current_price()
    crypto_list = list(current_crypto_prices.values())
    # print(current_stock_prices)
    # print("Current price: ", current_crypto_prices['BTC-EUR'], "  7-days average: ", seven_days_btc)
    # print(current_stock_prices[0])
    def on_publish(client, userdata, result):
        print("ok")
        pass

    stock_tracker = paho.Client("btc")
    stock_tracker.on_publish = on_publish
    stock_tracker.connect(broker, port)

    flag = 0
    topic = ""
    previous_item = [0, 0, 0, 0]
    for item in crypto_list:
        if item > 1.001 * previous_item[flag] or item < 0.999 * previous_item[flag]:
            topic = "investment/crypto/" + f'{flag}'
            print(topic)
            ret = stock_tracker.publish(topic, item)
            previous_item[flag] = item
        time.sleep(1)
        flag = flag + 1
    time.sleep(120)
    #
    # if (current_crypto_prices['BTC-EUR'] > 1.1*seven_days_btc):
    #     ret = crypto_tracker.publish("crypto/btc", "SELL")
    #     print("sell ok")
    # elif (current_crypto_prices['BTC-EUR'] < 0.9*seven_days_btc):
    #     ret = crypto_tracker.publish("crypto/btc", "BUY")
    #     print("buy ok")
    # else:
    #     ret = crypto_tracker.publish("crypto/btc", "NOTHING")
    #     print("do nothing")
