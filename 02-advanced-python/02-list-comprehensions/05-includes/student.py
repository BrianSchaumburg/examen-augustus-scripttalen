# Write your code here
def includes(xs = [], ys = [] ):
    return set(ys).issubset(set(xs))
includes([1,2,3,4,5],[1,2,3])