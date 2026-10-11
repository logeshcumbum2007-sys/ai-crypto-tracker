def optimize_portfolio(investment, assets):
    print("\n========== PORTFOLIO OPTIMIZATION ==========\n")

    total_market_cap = sum(assets.values())

    if investment <= 0 or total_market_cap <= 0:
        print("Invalid investment or asset data.")
        return

    total_allocated = 0

    for symbol, market_cap in assets.items():
        weight = market_cap / total_market_cap
        amount = round(investment * weight, 2)
        total_allocated += amount

        print(f"Asset: {symbol}")
        print(f"Allocation: {weight * 100:.2f}%")
        print(f"Investment Amount: ${amount:,.2f}")
        print("-" * 35)

    print(f"Total Investment: ${investment:,.2f}")
    print(f"Total Allocated: ${total_allocated:,.2f}")


if __name__ == "__main__":
    assets = {
        "BTC": 600,
        "ETH": 250,
        "SOL": 100,
        "ADA": 30,
        "DOT": 20
    }

    optimize_portfolio(10000, assets)
