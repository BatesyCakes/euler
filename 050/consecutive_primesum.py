import math

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


def max_prime_sum(n):
    '''brute force generation of the maximum consecutive prime sum
    below n'''
    primes = []
    x = 2
    while sum(primes) < n:
        if is_prime(x):
            primes.append(x)
        x += 1

    for i in range(1,1000000):
        if is_prime(sum(primes[0:-i])):
            return primes[-i]
        else:
            continue
    return "Does not compute."

print(max_prime_sum(1000000))
