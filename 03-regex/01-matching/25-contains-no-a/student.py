# Write your code here
import re
def contains_no_a(str):
    return re.fullmatch('((?!a+).)*',str)
