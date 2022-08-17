import csv
import re
import pandas
from operator import itemgetter
# reading given tsv file
lijst = []
with open("title-basics.tsv", 'r',encoding='utf-8') as myfile:
    reader = csv.DictReader(myfile,delimiter="\t")
    for line in reader:
        if(line['runtimeMinutes'] != '\\N' and line['titleType'] == 'movie'):
         lijst.append(line)
newlist = sorted(lijst, key=lambda d: d['runtimeMinutes'],reverse=False)
for line in range(0,100,+1):
    print(newlist[line]['primaryTitle']+':'+newlist[line]['runtimeMinutes'])




