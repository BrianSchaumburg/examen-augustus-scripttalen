import json
import matplotlib.pyplot as plt
import collections
import operator
f = open('covid.json')
data = json.load(f)

leeftijdsgroepen = {}
n = 0
for k in data:
    if k['AGEGROUP'] not in leeftijdsgroepen.keys():
        for j in data:
            if(j['AGEGROUP']==k['AGEGROUP']):
                n+=1
        leeftijdsgroepen[k['AGEGROUP']]=n
    n = 0
print(leeftijdsgroepen)
leeftijdsgroepen=collections.OrderedDict(sorted(leeftijdsgroepen.items()))
y=leeftijdsgroepen.values()
x=leeftijdsgroepen.keys()
plt.xlabel("de leeftijdsgroepen")
plt.ylabel("De waarden")
plt.title("De leeftijdsgroepen en hun vaccinaties")
plt.plot(x,y)
plt.show()
plt.close()
f.close()