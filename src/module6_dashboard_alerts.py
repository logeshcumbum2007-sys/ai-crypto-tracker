def generate_alerts(market_changes):
    print("\n========== CRYPTO DASHBOARD ==========\n")

    alert_count = 0

    for symbol, change in market_changes.items():
        print(f"{symbol}: 24h Change = {change:+.2f}%")

        if change >= 5:
            print(f"[HIGH] {symbol} price increased significantly.")
            alert_count += 1
        elif change <= -5:
            print(f"[HIGH] {symbol} price decreased significantly.")
            alert_count += 1
        elif abs(change) >= 2:
            print(f"[MEDIUM] {symbol} market movement detected.")
            alert_count += 1

        print("-" * 35)

    if alert_count == 0:
        print("[INFO] No significant market movements detected.")

    print(f"\nAlerts Generated: {alert_count}")


if __name__ == "__main__":
    # Demonstration data; replace with live changes when integrating.
    sample_changes = {
        "BTC": -6.2,
        "ETH": 2.5,
        "SOL": 0.8
    }

    generate_alerts(sample_changes)
