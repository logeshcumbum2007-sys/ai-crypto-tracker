import os
import json
from datetime import datetime
from openai import OpenAI


def predict_trends(market_data):
    """
    Module 2: AI-Based Price Trend Prediction & Anomaly Detection

    Receives live market data from Module 1 and uses OpenAI
    to analyze each cryptocurrency.
    """

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    results = []

    for _, row in market_data.iterrows():

        symbol = row["symbol"]
        price = row["price_usd"]
        volume = row["volume_24h"]
        market_cap = row["market_cap"]

        prompt = f"""
You are a cryptocurrency market analysis AI.

Analyze the following current market information:

Cryptocurrency: {symbol}
Current Price USD: {price}
24h Trading Volume USD: {volume}
Market Capitalization USD: {market_cap}

Give a short market assessment.

Return ONLY valid JSON in exactly this format:
{{
    "predicted_direction": "UP or DOWN",
    "confidence": 0.00,
    "anomaly_flag": true or false,
    "analysis": "short explanation"
}}

The confidence should be a value between 0.00 and 1.00.
This is an AI assessment confidence, NOT a guaranteed probability.
"""

        try:
            response = client.responses.create(
                model="gpt-5-mini",
                input=prompt
            )

            ai_text = response.output_text.strip()

            # Remove possible markdown code fences
            if ai_text.startswith("```"):
                ai_text = ai_text.replace("```json", "")
                ai_text = ai_text.replace("```", "")
                ai_text = ai_text.strip()

            analysis = json.loads(ai_text)

            result = {
                "timestamp": datetime.utcnow().isoformat(),
                "symbol": symbol,
                "predicted_direction": analysis["predicted_direction"],
                "confidence": analysis["confidence"],
                "anomaly_flag": analysis["anomaly_flag"],
                "analysis": analysis["analysis"]
            }

            results.append(result)

        except Exception as e:
            print(f"AI analysis failed for {symbol}: {e}")

    print("\n=== Module 2: AI-Based Price Trend Prediction ===")

    for result in results:
        print(result)

    return results


if __name__ == "__main__":
    print("Module 2 is ready.")
    print("It requires market data from Module 1.")
