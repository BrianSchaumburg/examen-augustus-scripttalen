import sys
for i in sys.argv[1:]:
    dubbele = set()
    with open(str(i),'r') as file:
        lines = file.readlines()
        for i in lines:
            dubbele.add(i)
    for i in dubbele:
        print(i.strip())