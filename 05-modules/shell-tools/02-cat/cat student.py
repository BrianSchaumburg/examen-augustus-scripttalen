import sys
for i in sys.argv[1:]:
    with open(str(i),'r') as file:
        for i in file.readlines():
            print(i)