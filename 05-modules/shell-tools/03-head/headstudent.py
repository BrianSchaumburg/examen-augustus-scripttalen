import sys
import argparse

parser = argparse.ArgumentParser(prog='head programma student')
parser.add_argument('start',type=str,default='')
parser.add_argument('-n','-argument',default=5, type=int,required=False)

# Parses sys.argv and stores parameters in args
args = parser.parse_args()
with open(args.start, 'r') as file:
    head = [next(file) for x in range(args.n)]
for i in head:
    print(str(i).strip())