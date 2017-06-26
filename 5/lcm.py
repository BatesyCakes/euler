from functools import reduce
import fractions
import time
start_time = time.time()

#returns greatest common divisor using Euclid's theorem
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#returns lowest common multicle
def lcm(a, b):
    return a * b // gcd(a, b)

#uses python's reduce to return lcm of a list
def lcmL(*L):
    return reduce(lcm, L)

print (lcmL(*range(1,21)))
print("--- %s seconds ---" %(time.time() - start_time))
