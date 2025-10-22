# Market Data ETL Pipeline

## Overview
This project extracts real-time cryptocurrency market data from a public API (CoinGecko), 
transforms it using Pandas, and loads it into a local SQLite database for analysis.  
It demonstrates how an ETL (Extract, Transform, Load) process works end to end using Python.

---

## Steps
1. Extract data from the CoinGecko API.  
2. Select key columns such as coin name, symbol, price, market cap, and trading volume.  
3. Rename columns for clarity.  
4. Load the transformed data into an SQLite database.  
5. Save and close the connection.

---

## Tools Used
- Python  
- Pandas  
- Requests  
- SQLite  

---

## Output
- **market_data.db** – database containing a table called `crypto_markets`.

---

## Key Skills Demonstrated
- API integration and data extraction  
- Data transformation with Pandas  
- SQL database handling using SQLite  
- End-to-end ETL workflow simulation  

---

## Notes
This project focuses on building an automated pipeline for external data ingestion.  
It reflects the kind of small-scale ETL tasks a junior data engineer would handle in production.
