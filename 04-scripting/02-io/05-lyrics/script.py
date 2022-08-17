import json
import sys
import urllib
import ssl

import requests

argumenten = sys.argv[1:]
url = "https://api.lyrics.ovh/v1/"
print(argumenten)
for i in argumenten[:1]:
    url += str(i)+"%20"
url+=argumenten[1]
url+="/"
for i in argumenten[2:-1]:
    url += str(i)+"%20"
url+=argumenten[-1]
print(url)

ssl._create_default_https_context = ssl._create_unverified_context
with urllib.request.urlopen(url) as input:
    data = json.loads(input.read())
    print(data['lyrics'])