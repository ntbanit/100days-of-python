import secrets
import base64

def generate_secure_token(length_bytes=32):
    """
    Generates a cryptographically secure random token of the specified length (in bytes).

    Args:
        length_bytes (int): The desired length of the token in bytes. Defaults to 32 (256 bits).

    Returns:
        str: The Base64-encoded token.
    """
    random_bytes = secrets.token_bytes(length_bytes)
    token = base64.urlsafe_b64encode(random_bytes).rstrip(b"=").decode("utf-8")
    return token

# Example usage:
secure_token = generate_secure_token()
print(f"Generated token: {secure_token}")
print(f"Token length: {len(secure_token)}")
