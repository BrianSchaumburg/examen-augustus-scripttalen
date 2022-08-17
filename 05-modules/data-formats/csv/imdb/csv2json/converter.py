import csv
import json
dictionary = {}
arrayadder = []
with open('csvbestand.csv','r',encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file,delimiter = ';')
    line_count = 0
    for rows in csv_reader:
        dictionary['voornaam'] = rows['voornaam']
        dictionary['achternaam'] = rows['achternaam']
        dictionary['straat'] = rows['stad']
        arrayadder.append(dictionary.copy()) #adding copy is necesary for linked reference
    with open('json_data.json','w',encoding="utf-8")as json_file:
        json.dump(arrayadder,json_file)

