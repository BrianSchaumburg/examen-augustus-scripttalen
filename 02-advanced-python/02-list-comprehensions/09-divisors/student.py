# Write your code here
def is_devisor(x,y):
    return x %y == 0
def devisors(x):
    return [n for n in range(1,100) if is_devisor(x,n)]
print(devisors(100))