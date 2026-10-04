def optimize_portfolio(predictions):
    """
    Module 4: Portfolio Optimization & Risk Scoring

    Uses predictions from Module 2 to calculate:
    - Risk score
    - Expected return
    - Portfolio weight
    """

    assets = []

    for prediction in predictions:
        symbol = prediction["symbol"]
        confidence = float(prediction["confidence"])
        direction = prediction["predicted_direction"]
        anomaly = prediction["anomaly_flag"]

        # Estimate expected return from prediction confidence
        if direction == "UP":
            expected_return = round(confidence * 0.25, 3)
        else:
            expected_return = round(-confidence * 0.10, 3)

        # Higher confidence = lower basic risk
        risk_score = round(1.0 - confidence, 2)

        # Increase risk when an anomaly is detected
        if anomaly:
            risk_score = min(1.0, round(risk_score + 0.20, 2))

        assets.append({
            "symbol": symbol,
            "risk_score": risk_score,
            "expected_return": expected_return
        })

    # Calculate portfolio scores
    scores = []

    for asset in assets:
        score = max(
            0.01,
            (asset["expected_return"] + 0.10)
            / (asset["risk_score"] + 0.10)
        )
        scores.append(score)

    total_score = sum(scores)

    # Calculate weights
    portfolio = []

    for asset, score in zip(assets, scores):
        weight = round(score / total_score, 3)

        portfolio.append({
            "symbol": asset["symbol"],
            "weight": weight,
            "expected_return": asset["expected_return"],
            "risk_score": asset["risk_score"]
        })

    print("\n=== Module 4: Portfolio Optimization & Risk Scoring ===")

    for item in portfolio:
        print(item)

    return portfolio


if __name__ == "__main__":
    print("Module 4 is ready.")
    print("It requires predictions from Module 2.")
