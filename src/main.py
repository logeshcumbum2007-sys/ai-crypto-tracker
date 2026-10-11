from market_data import get_market_data
from ai_predictor import predict_trends
from hash_verification import generate_hash, verify_hash
from portfolio_optimizer import optimize_portfolio
from user_tracking import authenticate, track_usage
from market_alerts import check_alerts


def main():
    print("=" * 45)
    print("       CRYPTO AI TRACKER")
    print("=" * 45)

    # 1. Fetch cryptocurrency market data
    print("\n1. MARKET DATA")
    market_data = get_market_data()
    print(market_data)

    # 2. Predict market trends
    print("\n2. AI TREND ANALYSIS")
    if market_data:
        predictions = predict_trends(market_data)
        print(predictions)
    else:
        print("Market data unavailable; analysis skipped.")

    # 3. Verify data integrity using a hash
    print("\n3. HASH VERIFICATION")
    transaction = {
        "coin": "BTC",
        "amount": 0.01,
        "type": "demo"
    }
    transaction_hash = generate_hash(transaction)
    print("SHA-256:", transaction_hash)
    print("Verified:", verify_hash(transaction, transaction_hash))

    # 4. Calculate portfolio allocation
    print("\n4. PORTFOLIO ALLOCATION")
    allocation = optimize_portfolio()
    print(allocation)

    # 5. Demonstrate user authentication and tracking
    print("\n5. USER ACCESS")
    if authenticate("student", "demo123"):
        track_usage("student", "run_tracker")
        print("Demo login successful.")
    else:
        print("Demo login failed.")

    # 6. Check market alerts
    print("\n6. MARKET ALERTS")
    alerts = check_alerts()
    print(alerts)

    print("\nTracker execution completed.")


if __name__ == "__main__":
    main()
