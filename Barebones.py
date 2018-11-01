from urllib.request import urlopen
import json
from pprint import pprint
url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park"
f = urlopen(url)
response_text = f.read()
response_data = json.loads(str(response_text, "utf-8"))
pprint(response_data)
