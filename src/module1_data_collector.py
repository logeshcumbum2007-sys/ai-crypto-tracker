import requests


def collect_market_data():
    print("\n========== CRYPTO MARKET DATA ==========\n")

    coins = {
        "bitcoin": "BTC",
        "ethereum": "ETH",
        "solana": "SOL"
    }

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": ",".join(coins.keys()),
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_24hr_vol": "true",
        "include_market_cap": "true"
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        for coin_id, symbol in coins.items():
            coin = data.get(coin_id, {})

            if "usd" not in coin:
                print(f"{symbol}: Data unavailable")
                continue

            print(f"Symbol: {symbol}")
            print(f"Price: ${coin['usd']:,.2f}")
            print(f"24h Change: {coin.get('usd_24h_change', 0):.2f}%")
            print(f"24h Volume: ${coin.get('usd_24h_vol', 0):,.2f}")
            print(f"Market Cap: ${coin.get('usd_market_cap', 0):,.2f}")
            print("-" * 35)

    except requests.RequestException as error:
        print("Unable to retrieve live data:", error)


if __name__ == "__main__":
    collect_market_data()
