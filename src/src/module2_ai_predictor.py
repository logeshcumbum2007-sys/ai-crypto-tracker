from datetime import datetime


def predict_trends(market_data):
    """
    Module 2: AI-Based Price Trend Prediction & Anomaly Detection
    Local analysis using live market data from Module 1.
    """

    results = []

    for _, row in market_data.iterrows():

        symbol = row["symbol"]
        price = float(row["price_usd"])
        volume = float(row["volume_24h"])
        market_cap = float(row["market_cap"])

        volume_ratio = volume / market_cap if market_cap > 0 else 0

        if volume_ratio > 0.10:
            direction = "UP"
            confidence = 0.85
            anomaly = True
            analysis = "High trading activity detected relative to market capitalization."

        elif volume_ratio > 0.05:
            direction = "UP"
            confidence = 0.72
            anomaly = False
            analysis = "Healthy trading activity detected."

        else:
            direction = "DOWN"
            confidence = 0.62
            anomaly = False
            analysis = "Relatively low trading activity detected."

        result = {
            "timestamp": datetime.utcnow().isoformat(),
            "symbol": symbol,
            "predicted_direction": direction,
            "confidence": confidence,
            "anomaly_flag": anomaly,
            "analysis": analysis
        }

        results.append(result)

    print("\n=== Module 2: AI-Based Price Trend Prediction ===")

    for result in results:
        print(result)

    return results


if __name__ == "__main__":
    print("Module 2 is ready.")
    print("It requires market data from Module 1.")
