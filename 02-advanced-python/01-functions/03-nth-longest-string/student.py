# Write your code here
from operator import itemgetter

def nth_longest_string(xs,n):
    return sorted(xs, key=len)[-n]
def main():
    xs = ['abc','aa','cc','bbb']
    print(nth_longest_string(xs,1))
main()