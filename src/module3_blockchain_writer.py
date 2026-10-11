import hashlib
import json


def generate_hash(data):
    content = json.dumps(data, sort_keys=True)
    return hashlib.sha256(content.encode()).hexdigest()


def verify_data(data, saved_hash):
    return generate_hash(data) == saved_hash


if __name__ == "__main__":
    print("\n========== HASH VERIFICATION ==========\n")

    transaction = {
        "symbol": "BTC",
        "price": 84800.00,
        "status": "Recorded"
    }

    saved_hash = generate_hash(transaction)

    print("Transaction:", transaction)
    print("\nGenerated SHA-256 Hash:")
    print(saved_hash)

    if verify_data(transaction, saved_hash):
        print("\nVerification Status: Successful")
        print("Data Integrity: Verified")
    else:
        print("\nVerification Status: Failed")
