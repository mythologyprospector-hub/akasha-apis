import os, requests

def fetch_repo(repo):
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}

    url = f"https://api.github.com/repos/{repo}"
    r = requests.get(url, headers=headers)

    return r.json()