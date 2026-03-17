import os, requests

def fetch_apod():
    key = os.getenv("NASA_API_KEY")
    url = f"https://api.nasa.gov/planetary/apod?api_key={key}"
    return requests.get(url).json()