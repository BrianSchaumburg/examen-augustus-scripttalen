import sys

with open("tekst.txt", "r") as file:
    lines = file.readlines()
    with open('readme.txt',"w") as f:
        f.writelines(lines)