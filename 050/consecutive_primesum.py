import math
import time as t


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


def prime_list_gen(n):
    '''brute force generation of list of primes up to a number n'''
    primes = [2]
    for x in range(3, n, 2):
        if is_prime(x):
            primes.append(x)
    return primes


def max_prime_sum(n):
    '''finds the longest consecutive prime some'''
    primes = prime_list_gen(n)
    length = 0        #reference for length of current longest
    longest = 0       #prime with the longest consecutive prime sum
    last = len(primes)
    for i in range(last):
        for j in range(i+length, last):
            sum_slice = sum(primes[i:j])
            if sum_slice < n:
                if sum_slice in primes:
                    length = j-i
                    longest = sum_slice
            else:
                break
    return longest

def main():
    start = t.time()
    print("The longest consecutive prime sum is %s" %(max_prime_sum(1000000)))
    print("--- %s seconds ---" %(t.time()-start))

if __name__ == '__main__':
    main()
