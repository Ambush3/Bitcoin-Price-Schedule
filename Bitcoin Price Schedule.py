#!/usr/bin/env python3

import requests
import json
import os
import stat


st = os.stat('Bitcoin Price Schedule.py')
os.chmod('Bitcoin Price Schedule.py', st.st_mode | stat.S_IEXEC)

# put here your webhook_url obtained from the steps above
webhook_url =  "https://hooks.slack.com/services/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"

btc_url = "https://query1.finance.yahoo.com/v7/finance/quote?&symbols=BTC-USD&fields=extendedMarketChange,extendedMarketChangePercent,extendedMarketPrice,extendedMarketTime,regularMarketChange,regularMarketChangePercent,regularMarketPrice,regularMarketTime,circulatingSupply,ask,askSize,bid,bidSize,dayHigh,dayLow,regularMarketDayHigh,regularMarketDayLow,regularMarketVolume,volume"

response = requests.get(btc_url)
data = response.json()
btc_price = data["quoteResponse"]["result"][0]["regularMarketPrice"]

payload = {
    "channel": "#random",
    "username": "BTC PRICE",
    "text": f"${btc_price:,.2f}",
    "icon_emoji": ":dollar:"
}
requests.post(webhook_url, data=json.dumps(payload))
