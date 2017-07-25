from time import time
import math

start = time()
# checks if a number is prime
def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif not n & 1:	# if n is even (and not 2)
        return False
    for x in range(3, int(math.sqrt(n))+1, 2):
        if n % x == 0:
            return False
    return True

def main():
    a_max, b_max, longest = 0, 0, 0
    for x in range(-999, 1000):
        for y in range(-1000, 1001):
            n = 0
            while isPrime(abs((n*(x+n) + y))):
                n += 1
            if n > longest:
                longest = n
                a_max, b_max = x, y

    print("a = %s, b = %s, longest sequence = %s, max product = %s\n---%s seconds---"\
    %(a_max, b_max, (a_max * b_max), longest, (time() - start)))

if __name__ == "__main__":
    main()
