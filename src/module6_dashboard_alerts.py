# module6_dashboard_alerts.py

from datetime import datetime, timezone


def generate_alert(prediction):
    """
    Generates an alert based on an AI prediction.

    Args:
        prediction (dict): AI prediction result containing:
            - symbol
            - predicted_direction
            - confidence
            - anomaly_flag

    Returns:
        dict: Generated alert information.
    """

    symbol = prediction["symbol"]
    direction = prediction["predicted_direction"]
    confidence = prediction["confidence"]
    anomaly = prediction["anomaly_flag"]

    alert_type = "INFO"
    message = f"No major signal detected for {symbol}."

    # High-confidence trading signal
    if confidence >= 0.80:
        alert_type = "AI SIGNAL"
        message = (
            f"{symbol} shows a high-confidence "
            f"{direction} signal ({confidence * 100:.0f}% confidence)."
        )

    # Anomaly detection alert
    if anomaly:
        alert_type = "ANOMALY"
        message = (
            f"Unusual market activity detected for {symbol}. "
            f"Further analysis is recommended."
        )

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "symbol": symbol,
        "alert_type": alert_type,
        "message": message,
        "confidence": confidence
    }


def generate_alerts(predictions):
    """
    Generates alerts for multiple AI predictions.

    Args:
        predictions (list): List of prediction dictionaries.

    Returns:
        list: Generated alerts.
    """

    alerts = []

    for prediction in predictions:
        alert = generate_alert(prediction)
        alerts.append(alert)

    return alerts


def display_dashboard(predictions, alerts):
    """
    Displays a simple user dashboard.

    Args:
        predictions (list): AI prediction results.
        alerts (list): Generated alerts.
    """

    print("\n" + "=" * 60)
    print("             CRYPTO AI SIGNAL DASHBOARD")
    print("=" * 60)

    print("\n--- Market Predictions ---")

    for prediction in predictions:
        print(
            f"{prediction['symbol']:5} | "
            f"Direction: {prediction['predicted_direction']:4} | "
            f"Confidence: {prediction['confidence'] * 100:.0f}% | "
            f"Anomaly: {prediction['anomaly_flag']}"
        )

    print("\n--- Alerts ---")

    if not alerts:
        print("No alerts available.")
        return

    for alert in alerts:
        print(
            f"[{alert['alert_type']}] "
            f"{alert['symbol']} -> {alert['message']}"
        )

    print("\n" + "=" * 60)


def main():
    """
    Module 6 demonstration.
    """

    print("=== Module 6: User Dashboard / Alert System ===")

    # Example AI predictions.
    # These could come from Module 2.
    predictions = [
        {
            "symbol": "BTC",
            "predicted_direction": "UP",
            "confidence": 0.91,
            "anomaly_flag": False
        },
        {
            "symbol": "ETH",
            "predicted_direction": "DOWN",
            "confidence": 0.76,
            "anomaly_flag": False
        },
        {
            "symbol": "SOL",
            "predicted_direction": "UP",
            "confidence": 0.87,
            "anomaly_flag": True
        }
    ]

    # Generate alerts
    alerts = generate_alerts(predictions)

    # Display dashboard
    display_dashboard(predictions, alerts)

    return alerts


if __name__ == "__main__":
    main()
