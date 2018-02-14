from fractions import gcd
from fractions import Fraction
from math import gcd
import math


'''I'm trying to solve this problem, as this is the last problem
for me to get the Trinary Triumph achievement. I've always
appreciated alliteration. The program is much to slow, and I need
to find mathematical shortcuts instead of brute force.
Even modern CPU's have their limits.'''

def resilients(den):
    '''Returns the total number of resilient numerators.'''
    total = 0

    for num in range(1,den):
        if gcd(num,den) == 1:
            total += 1
        else:
            continue
    return total


def is_prime(n):
    '''checks if a number is prime'''
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


def prime_list(n):
    '''brute force generation of a list of primes to n'''
    primes = []
    x = 2
    while len(primes) < n:
        if is_prime(x):
            primes.append(x)
        x += 1
    return primes


def main():
    floor = 1
    ceiling = 1

    for num in prime_list(23):
        floor *= num

    for num in prime_list(30):
        ceiling *= num

    for i in range(floor,ceiling):
        if Fraction(resilients(i),(i-1)) < Fraction('15499/94744'):
            return i
        else:
            continue


if __name__ == '__main__':
    main()
