import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data(symbols=["BTC", "ETH", "SOL"]):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": ",".join([s.lower() for s in symbols]),
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    rows = []
    for coin in data:
        rows.append({
            "timestamp": datetime.utcnow().isoformat(),
            "symbol": coin["symbol"].upper(),
            "price_usd": coin["current_price"],
            "volume_24h": coin["total_volume"],
            "market_cap": coin["market_cap"]
        })

    df = pd.DataFrame(rows)
    print("=== Module 1: Real-Time Crypto Data ===")
    print(df.to_string(index=False))
    return df

if __name__ == "__main__":
    fetch_crypto_data()
