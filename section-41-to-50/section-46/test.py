import requests

try:
    response = requests.get("https://accounts.spotify.com/api/token", timeout=5)
    print(f"Status Code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")