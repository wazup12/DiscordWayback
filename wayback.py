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

def output(url):
	response = check_url(url)
	out = (False, "No URL")
	snap = response["archived_snapshots"]
	if not snap: return out
	closest = snap["closest"]
	if not closest: return out
	out = (closest["available"], closest["url"])
	return out

def debug():
	output("https://jarrettbillingsley.github.io/teaching/classes/cs0447/projects/proj2.html")

if __name__=="__main__":
	debug()
