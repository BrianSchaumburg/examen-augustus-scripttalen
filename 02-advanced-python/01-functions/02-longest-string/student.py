# Write your code here
def longest_string(xs):
    return max(xs, key=lambda p: len(p))
def main():
    xs =['a','abc','cc']
    print(longest_string(xs))
main()