"""
Project: Market Data ETL Pipeline
Author: Joe Ngangu
Description:
Extracts live cryptocurrency market data from a public API, transforms it using Pandas, 
and loads it into a local SQLite database for analysis.
"""

import requests
import pandas as pd
import sqlite3

#  Extract – Get data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 50, "page": 1}
response = requests.get(url, params=params)
data = response.json()

#  Transform – Select and rename key fields
df = pd.DataFrame(data)[["id", "symbol", "current_price", "market_cap", "total_volume"]]
df.rename(columns={"id": "coin", "symbol": "ticker"}, inplace=True)

#  Load – Save to SQLite database
conn = sqlite3.connect("market_data.db")
df.to_sql("crypto_markets", conn, if_exists="replace", index=False)
conn.close()

print("✅ Market data ETL complete – crypto data saved to 'market_data.db'")
