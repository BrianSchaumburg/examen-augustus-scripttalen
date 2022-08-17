# Write your code here
def average(ns = []):
    return round(sum(ns) / len(ns))
def format_grades(grades=dict):
    string = ''
    for key, value in grades.items():
        returnaverage = average(value)
        string+=str(str(key)+": "+str(returnaverage)+"\n")
    return string
print(format_grades({ 'John': [10, 10, 10], 'Ann': [12, 14], 'Nick': [17, 18, 18] }))
