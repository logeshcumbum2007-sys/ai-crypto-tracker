# module5_authentication.py

import hashlib
import secrets
from datetime import datetime, timezone


# In-memory user database for demonstration
users = {}

# API usage tracking
api_usage = {}


def hash_password(password):
    """
    Securely hashes a password using SHA-256.

    Args:
        password (str): User's plain-text password.

    Returns:
        str: Hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    """
    Registers a new user.

    Args:
        username (str): Username.
        password (str): User password.

    Returns:
        dict: Registration result.
    """

    if username in users:
        return {
            "success": False,
            "message": "Username already exists."
        }

    users[username] = {
        "password_hash": hash_password(password),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "api_key": secrets.token_hex(16)
    }

    api_usage[username] = {
        "total_requests": 0,
        "last_request": None
    }

    return {
        "success": True,
        "message": "User registered successfully.",
        "api_key": users[username]["api_key"]
    }


def authenticate_user(username, password):
    """
    Authenticates a user using username and password.

    Args:
        username (str): Username.
        password (str): User password.

    Returns:
        bool: True if authentication succeeds.
    """

    if username not in users:
        return False

    password_hash = hash_password(password)

    return users[username]["password_hash"] == password_hash


def validate_api_key(api_key):
    """
    Validates an API key and identifies the associated user.

    Args:
        api_key (str): API key.

    Returns:
        str or None: Username if valid, otherwise None.
    """

    for username, user_data in users.items():
        if secrets.compare_digest(user_data["api_key"], api_key):
            return username

    return None


def track_api_usage(username):
    """
    Tracks API requests made by a user.

    Args:
        username (str): Authenticated username.

    Returns:
        dict: Updated usage information.
    """

    if username not in api_usage:
        api_usage[username] = {
            "total_requests": 0,
            "last_request": None
        }

    api_usage[username]["total_requests"] += 1
    api_usage[username]["last_request"] = (
        datetime.now(timezone.utc).isoformat()
    )

    return api_usage[username]


def get_usage_statistics(username):
    """
    Returns API usage statistics for a user.

    Args:
        username (str): Username.

    Returns:
        dict: Usage statistics.
    """

    return api_usage.get(username, {
        "total_requests": 0,
        "last_request": None
    })


def main():
    print("=== Module 5: Secure User Authentication & API Usage Tracking ===")

    # --------------------------------------------------
    # 1. Register user
    # --------------------------------------------------

    username = "crypto_user"
    password = "SecurePassword123"

    registration = register_user(username, password)

    print("\nRegistration:")
    print(registration)

    # --------------------------------------------------
    # 2. Authenticate user
    # --------------------------------------------------

    authenticated = authenticate_user(username, password)

    print("\nAuthentication:")
    print("Login successful." if authenticated else "Login failed.")

    # --------------------------------------------------
    # 3. Validate API key
    # --------------------------------------------------

    if authenticated:
        api_key = users[username]["api_key"]

        authenticated_user = validate_api_key(api_key)

        print("\nAPI Access:")
        print(f"API key validated for user: {authenticated_user}")

        # --------------------------------------------------
        # 4. Track API requests
        # --------------------------------------------------

        print("\nAPI Usage Tracking:")

        for _ in range(3):
            usage = track_api_usage(username)
            print(usage)

        # --------------------------------------------------
        # 5. Display statistics
        # --------------------------------------------------

        statistics = get_usage_statistics(username)

        print("\nUsage Statistics:")
        print(statistics)


if __name__ == "__main__":
    main()
