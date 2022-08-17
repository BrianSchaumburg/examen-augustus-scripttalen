import re
with open('example-test-file.txt','r') as file:
    lines = file.readlines()
    with open ('example-test-file.txt','w') as output:
        for line in lines:
            if not re.search(r'.*#.*',line):
                output.write(line)