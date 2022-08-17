import sys
filex = str(sys.argv[1])
print(filex)
with open(filex, "r") as file:
  for line in file:
    print (line)