import math


def divisor_gen(n):
    '''generates list of divisors of a number'''
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.append(n)
    return list(set(divs))



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


def prime_gen(n):
    '''brute force generation of the nth prime number'''
    primes = []
    x = 2
    while len(primes) < n:
        if prime_check(x):
            primes.append(x)
        x += 1
    return primes[-1]

def is_pandigital(n):
    '''check if a number is pandigital'''
    x = sorted(str(n))
    for i in range(1, len(x) + 1):
        if x[i - 1] != str(i):
            return False
    return True
