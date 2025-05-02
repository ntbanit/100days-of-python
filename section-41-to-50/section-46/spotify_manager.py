import requests
import os
from base64 import b64encode

# Spotify API credentials
SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

# Spotify token endpoint
url = "https://accounts.spotify.com/api/token"

# Encode client ID and secret in Base64
auth_header = b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()

# Request headers and body
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials"
}

# Make the POST request
try:
    response = requests.post(url, headers=headers, data=data)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Access Token:", response.json().get("access_token"))
    else:
        print("Error:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Request Error: {e}")