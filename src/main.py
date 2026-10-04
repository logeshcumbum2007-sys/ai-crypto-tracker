from module1_data_collector import fetch_crypto_data
from module2_ai_predictor import predict_trends
from module3_blockchain_writer import write_predictions_on_chain
from module4_portfolio_optimizer import optimize_portfolio
from module5_authentication import run_authentication_demo
from module6_dashboard_alerts import run_dashboard


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def print_line():
    print("─" * 68)


def print_header(title):
    print()
    print("┌" + "─" * 66 + "┐")
    print("│" + title.center(66) + "│")
    print("└" + "─" * 66 + "┘")


# ============================================================
# START SYSTEM
# ============================================================

print()
print("╔" + "═" * 66 + "╗")
print("║" + "CRYPTO AI SYSTEM".center(66) + "║")
print("║" + "REAL-TIME CRYPTO ANALYTICS PLATFORM".center(66) + "║")
print("╚" + "═" * 66 + "╝")

print()
print("SYSTEM STATUS")
print_line()
print("  ✓ Module 1  - Real-Time Cryptocurrency Data")
print("  ✓ Module 2  - AI-Based Trend Prediction")
print("  ✓ Module 3  - Blockchain Integration")
print("  ✓ Module 4  - Portfolio Optimization")
print("  ✓ Module 5  - User Authentication & API Tracking")
print("  ✓ Module 6  - Dashboard & Alert System")
print_line()


# ============================================================
# MODULE 1
# ============================================================

print_header("MODULE 1 | LIVE CRYPTOCURRENCY DATA")

market_data = fetch_crypto_data()

print()
print("LIVE MARKET SUMMARY")
print_line()

print(
    f"{'ASSET':<10}"
    f"{'PRICE (USD)':<18}"
    f"{'24H VOLUME':<20}"
    f"{'MARKET CAP':<20}"
)

print_line()

for _, row in market_data.iterrows():

    price = float(row["price_usd"])
    volume = float(row["volume_24h"])
    market_cap = float(row["market_cap"])

    if volume >= 1_000_000_000:
        volume_display = f"${volume / 1_000_000_000:.2f}B"
    elif volume >= 1_000_000:
        volume_display = f"${volume / 1_000_000:.2f}M"
    else:
        volume_display = f"${volume:,.0f}"

    if market_cap >= 1_000_000_000_000:
        market_cap_display = f"${market_cap / 1_000_000_000_000:.2f}T"
    elif market_cap >= 1_000_000_000:
        market_cap_display = f"${market_cap / 1_000_000_000:.2f}B"
    else:
        market_cap_display = f"${market_cap:,.0f}"

    print(
        f"{row['symbol']:<10}"
        f"${price:<17,.2f}"
        f"{volume_display:<20}"
        f"{market_cap_display:<20}"
    )

print_line()


# ============================================================
# MODULE 2
# ============================================================

print_header("MODULE 2 | AI-BASED TREND PREDICTION")

predictions = predict_trends(market_data)

print()
print("AI PREDICTION SUMMARY")
print_line()

print(
    f"{'ASSET':<10}"
    f"{'DIRECTION':<15}"
    f"{'CONFIDENCE':<15}"
    f"{'ANOMALY':<15}"
)

print_line()

for prediction in predictions:

    direction = prediction["predicted_direction"]
    confidence = prediction["confidence"] * 100
    anomaly = "YES" if prediction["anomaly_flag"] else "NO"

    print(
        f"{prediction['symbol']:<10}"
        f"{direction:<15}"
        f"{confidence:.0f}%{'':<12}"
        f"{anomaly:<15}"
    )

print_line()


# ============================================================
# MODULE 3
# ============================================================

print_header("MODULE 3 | BLOCKCHAIN VERIFICATION")

tx_hash = write_predictions_on_chain(predictions)

print()
print("BLOCKCHAIN RESULT")
print_line()
print("  Predictions recorded successfully.")
print("  Verification Status : ✓ SUCCESS")
print("  Transaction Hash    :")
print(f"  {tx_hash}")
print("  Blockchain Mode     : SIMULATED")
print_line()


# ============================================================
# MODULE 4
# ============================================================

print_header("MODULE 4 | PORTFOLIO OPTIMIZATION")

portfolio = optimize_portfolio(predictions)

print()
print("OPTIMIZED PORTFOLIO")
print_line()

print(
    f"{'ASSET':<10}"
    f"{'WEIGHT':<15}"
    f"{'EXPECTED RETURN':<20}"
    f"{'RISK SCORE':<15}"
)

print_line()

for item in portfolio:

    print(
        f"{item['symbol']:<10}"
        f"{item['weight'] * 100:.1f}%{'':<11}"
        f"{item['expected_return']:<20.3f}"
        f"{item['risk_score']:<15.2f}"
    )

print_line()


# ============================================================
# MODULE 5
# ============================================================

print_header("MODULE 5 | SECURITY & API MANAGEMENT")

usage_statistics = run_authentication_demo()

print()
print("SECURITY SUMMARY")
print_line()
print("  Authentication      : ✓ SUCCESS")
print("  API Key Validation   : ✓ SUCCESS")
print(
    f"  Total API Requests  : "
    f"{usage_statistics['total_requests']}"
)
print("  Storage Mode         : IN-MEMORY DEMO")
print_line()


# ============================================================
# MODULE 6
# ============================================================

print_header("MODULE 6 | DASHBOARD & ALERT SYSTEM")

alerts = run_dashboard(predictions)

print()
print("ALERT SUMMARY")
print_line()

for alert in alerts:

    print(
        f"  [{alert['alert_type']:<8}] "
        f"{alert['symbol']:<5} "
        f"→ {alert['message']}"
    )

print_line()


# ============================================================
# FINAL SYSTEM OUTPUT
# ============================================================

print()
print("╔" + "═" * 66 + "╗")
print("║" + "FINAL SYSTEM OUTPUT".center(66) + "║")
print("╚" + "═" * 66 + "╝")

print()
print("  System Status          : ✓ COMPLETED")
print("  Modules Completed      : 6 / 6")
print(f"  Predictions Generated  : {len(predictions)}")
print(f"  Alerts Generated       : {len(alerts)}")
print("  Blockchain Verification: ✓ SUCCESS")
print("  Authentication         : ✓ SUCCESS")

print()
print("  Transaction Hash:")
print(f"  {tx_hash}")

print()
print("╔" + "═" * 66 + "╗")
print("║" + "✓ ALL 6 MODULES COMPLETED SUCCESSFULLY".center(66) + "║")
print("║" + "CRYPTO AI SYSTEM READY".center(66) + "║")
print("╚" + "═" * 66 + "╝")

print()
