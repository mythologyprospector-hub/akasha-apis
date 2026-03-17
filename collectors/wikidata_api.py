import requests

def query(sparql):
    url = "https://query.wikidata.org/sparql"
    headers = {"Accept": "application/json"}

    return requests.get(url, params={"query": sparql}, headers=headers).json()