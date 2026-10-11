def predict_trends(market_data):
    print("\n========== AI TREND ANALYSIS ==========\n")

    for symbol, price_change in market_data.items():
        if price_change > 1:
            trend = "UP"
            confidence = 60 + min(price_change, 15)
        elif price_change < -1:
            trend = "DOWN"
            confidence = 60 + min(abs(price_change), 15)
        else:
            trend = "NEUTRAL"
            confidence = 50

        print(f"Asset: {symbol}")
        print(f"Predicted Trend: {trend}")
        print(f"Confidence: {confidence:.1f}%")
        print("-" * 35)


if __name__ == "__main__":
    # Demonstration input; replace with actual market data when integrating.
    sample_data = {
        "BTC": -2.0,
        "ETH": 1.5,
        "SOL": 0.3
    }

    predict_trends(sample_data)
