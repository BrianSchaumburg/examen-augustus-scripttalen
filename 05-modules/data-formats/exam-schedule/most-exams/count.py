import csv
import collections

grades = collections.Counter()
with open('exam-schedule.csv') as input_file:
    for row in csv.reader(input_file, delimiter=','):
        grades[row[11]] += 1 # de studentennummer wordt hier als key gebruikt
print(grades)
new_value = max(grades, key=grades.get)
for k, v in grades.items():
    if(k == new_value):
        waarde = v
print(new_value,waarde)