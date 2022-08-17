# Write your code here
def drop_nth(xs, n):
    first = list
    last = list

    first = xs[0:n]
    last = xs[n+1:]
    return first + last;
def main():
    xs = [1,2,3,4]
    print(drop_nth(xs,2))

main()
