import json
import requests
import re
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
for i in sys.argv[1:]:
    if(i != sys.argv[-1]):
        url+=str(i)+'%20'
    else:
        url+=str(i)
request = requests.get(url,verify=False)
jsondump = json.loads(request.text)
index = 0
for i in jsondump['drinks']:
    sleutels=  i.keys()
regex = r'strIngredient[0-9]'
for i in sleutels:
    if re.fullmatch(regex,i):
        index+=1

for i in jsondump['drinks']:
    print(i['strDrink'])
    for j in range(1,index):
        if(i[f'strIngredient{j}']!=None):
            print(i[f'strIngredient{j}']+ " " + str(i[f'strMeasure{j}']))
