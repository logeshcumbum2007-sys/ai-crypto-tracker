usage_count = {}


def authenticate_user(username, password):
    # Demo credentials only; do not use hardcoded passwords in production.
    if username == "student" and password == "demo123":
        print("Authentication Status: Successful")
        return True

    print("Authentication Status: Failed")
    return False


def track_usage(username, action):
    usage_count[username] = usage_count.get(username, 0) + 1

    print(f"User: {username}")
    print(f"Action: {action}")
    print(f"Usage Count: {usage_count[username]}")


if __name__ == "__main__":
    print("\n====== USER AUTHENTICATION ======\n")

    user = "student"
    password = "demo123"

    if authenticate_user(user, password):
        track_usage(user, "Market Data Request")
        track_usage(user, "AI Prediction Request")
        track_usage(user, "Portfolio Optimization")
