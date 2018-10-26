import math
from time import time
start_time = time()

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
    '''brute force generation of a list of primes to n in conjunction with
    is_prime()'''
    primes = []
    x = 2
    while len(primes) < n:
        if is_prime(x):
            primes.append(x)
        x += 1
    return primes

def main():
    primes = prime_list(200)
    ans = 1

    for i in primes:
        if (ans * i) < 1000000:
            ans *= i
        else:
            break

    print(ans)
    print("--- %s seconds ---" %(time()-start_time))

if __name__ == '__main__':
    main()
