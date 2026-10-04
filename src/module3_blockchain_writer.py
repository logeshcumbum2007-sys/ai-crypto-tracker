import hashlib
import json


def write_predictions_on_chain(predictions):
    """
    Module 3: Blockchain Integration

    Receives predictions from Module 2 and creates
    a SHA-256 hash to simulate blockchain storage.
    """

    payload = json.dumps(predictions, sort_keys=True)

    tx_hash = "0x" + hashlib.sha256(payload.encode()).hexdigest()

    print("\n=== Module 3: Blockchain Integration ===")
    print("Number of predictions:", len(predictions))
    print("Payload (first 100 chars):", payload[:100], "...")
    print("Simulated on-chain transaction hash:")
    print(tx_hash)
    print("Status: Prediction hash written to blockchain (simulated).")

    return tx_hash


if __name__ == "__main__":
    print("Module 3 is ready.")
    print("It requires predictions from Module 2.")
