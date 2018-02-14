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


def primes_gen(n):
    '''Returns a list of primes up to n'''
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def is_pandigital(n):
    '''check if a number is pandigital'''
    x = sorted(str(n))
    for i in range(1, len(x) + 1):
        if x[i - 1] != str(i):
            return False
    return True
