import requests
import io
url = 'https://www.reddit.com'
r = requests.get(url, verify = False)
weergave = r.text
with io.open("weergave.txt",'w',encoding="utf-8") as file:
    file.write(weergave)
print(weergave)