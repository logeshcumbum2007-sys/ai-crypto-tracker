import random

def optimize_portfolio(symbols=["BTC", "ETH", "SOL", "ADA", "DOT"]):
    """
    Module 4: Portfolio Optimization & Risk Scoring Using AI

    This function:
    - Generates mock risk scores and expected returns for each coin
    - Computes a simple score: expected_return / (risk + small_constant)
    - Converts scores into portfolio weights that sum to 1
    - Prints a table-like output with symbol, weight, expected_return, risk_score
    """
    assets = []
    for sym in symbols:
        risk = round(random.uniform(0.3, 0.9), 2)
        ret = round(random.uniform(-0.05, 0.25), 3)
        assets.append({
            "symbol": sym,
            "risk_score": risk,
            "expected_return": ret
        })

    # Simple heuristic score: higher return, lower risk -> higher weight
    scores = [a["expected_return"] / (a["risk_score"] + 0.1) for a in assets]
    total_score = sum(scores)
    weights = [round(s / total_score, 3) for s in scores]

    portfolio = []
    for a, w in zip(assets, weights):
        portfolio.append({
            "symbol": a["symbol"],
            "weight": w,
            "expected_return": a["expected_return"],
            "risk_score": a["risk_score"]
        })

    print("=== Module 4: Portfolio Optimization & Risk Scoring ===")
    for p in portfolio:
        print(p)
    return portfolio

if __name__ == "__main__":
    optimize_portfolio()
