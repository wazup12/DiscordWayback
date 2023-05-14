# temp
import requests
from internetarchive import get_item, upload

BASE_URL = "https://archive.org/wayback/"

def check_url(query):
    url = f"{BASE_URL}available?url={query}"
    r = requests.get(url)
    return r.json()

def upload(url):
    url = f"{BASE_URL}available?url={query}"
    h = {'accept': 'application/json', 'Content-Type':'application/json'}

def debug():
    response = check_url("https://jarrettbillingsley.github.io/teaching/classes/cs0447/projects/proj2.html")
    if response["archived_snapshots"] and response["archived_snapshots"]["closest"] and response["archived_snapshots"]["closest"]["available"]:
        print(response["archived_snapshots"]["closest"]["available"])
        print(response["archived_snapshots"]["closest"]["url"])



if __name__=="__main__":
    debug()
