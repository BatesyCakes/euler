from math import pow
from time import time
start = time()


def power(x, y):
    return x ** y

def numberSum(n):
    s = str(n)
    total = 0
    for digit in s:
        total += int(digit)
    return total

print(numberSum((power(2,1000))))
print("---%s seconds---" %(time()-start))
