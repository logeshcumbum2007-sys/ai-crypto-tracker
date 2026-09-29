import hashlib
import json
import random
from datetime import datetime

def generate_mock_predictions(symbols=["BTC", "ETH", "SOL"]):
    """
    Generate mock AI predictions similar to Module 2.
    In a real system, this would come from your AI model.
    """
    predictions = []
    for sym in symbols:
        direction = random.choice(["UP", "DOWN"])
        confidence = round(random.uniform(0.55, 0.95), 2)
        anomaly = random.choice([True, False])
        predictions.append({
            "timestamp": datetime.utcnow().isoformat(),
            "symbol": sym,
            "predicted_direction": direction,
            "confidence": confidence,
            "anomaly_flag": anomaly
        })
    return predictions

def write_predictions_on_chain(predictions):
    """
    Module 3: Blockchain Integration for Transparent & Verifiable Signals
    
    This function:
    - Takes a list of predictions
    - Creates a JSON payload
    - Computes a hash (simulating on-chain storage)
    - Prints a simulated transaction hash and status
    """
    payload = json.dumps(predictions, sort_keys=True)
    tx_hash = "0x" + hashlib.sha256(payload.encode()).hexdigest()

    print("=== Module 3: Blockchain Integration ===")
    print("Number of predictions:", len(predictions))
    print("Payload (first 100 chars):", payload[:100], "...")
    print("Simulated on-chain transaction hash:")
    print(tx_hash)
    print("Status: Prediction hash written to blockchain (simulated).")
    return tx_hash

if __name__ == "__main__":
    preds = generate_mock_predictions()
    write_predictions_on_chain(preds)
