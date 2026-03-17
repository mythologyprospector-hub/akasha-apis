# API Usage Guide

Collectors fetch external data and normalize it into artifacts usable by the Akasha ecosystem.

Example:

```python
import requests

def collect_github_repo(repo):
    url = f"https://api.github.com/repos/{repo}"
    r = requests.get(url)

    data = r.json()

    return {
        "type": "repository",
        "name": data["name"],
        "stars": data["stargazers_count"],
        "forks": data["forks"]
    }
```