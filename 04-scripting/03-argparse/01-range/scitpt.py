import argparse

parser = argparse.ArgumentParser(prog='git')
parser.add_argument('start',type=int,default=0)
parser.add_argument('end',type=int)
parser.add_argument('--step', default=1, type=int)
parser.add_argument('--format','-x',action='store_true')

# Parses sys.argv and stores parameters in args
args = parser.parse_args()

start  =args.start
end = args.end
getal = start

while(getal + args.step < end):
    getal += args.step
    print(getal)
if(args.format == False):
    print(end)
