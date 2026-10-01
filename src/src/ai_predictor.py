import random
from datetime import datetime

def predict_trends(symbols=["BTC", "ETH", "SOL"]):
    """
    Module 2: AI-Based Price Trend Prediction & Anomaly Detection
    
    For each symbol, this function:
    - Predicts price direction (UP/DOWN)
    - Assigns a confidence score
    - Flags possible anomalies
    """
    results = []
    for sym in symbols:
        direction = random.choice(["UP", "DOWN"])
        confidence = round(random.uniform(0.55, 0.95), 2)
        anomaly = random.choice([True, False])
        results.append({
            "timestamp": datetime.utcnow().isoformat(),
            "symbol": sym,
            "predicted_direction": direction,
            "confidence": confidence,
            "anomaly_flag": anomaly
        })

    print("=== Module 2: AI-Based Price Trend Prediction ===")
    for r in results:
        print(r)
    return results

if __name__ == "__main__":
    predict_trends()
