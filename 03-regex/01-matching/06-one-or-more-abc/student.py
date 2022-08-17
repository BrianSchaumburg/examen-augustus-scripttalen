# Write your code here
import re
def one_or_more_abc(string = ''):
    return re.fullmatch(r'.+(abc)+(.+)?(abc)+.*',string)
print(one_or_more_abc("dit is een test abc  test"))