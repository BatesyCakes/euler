import math
import time as t

start = t.time()

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

def trunc_right(n):
    '''removes digits from right to left'''
    x = list(str(n))
    for i in range(1, len(x)):
        y = x[:-i]
        s = int(''.join(y))
        if is_prime(s):
            continue
        else:
            return False
    return True

def trunc_left(n):
    '''removes digits from left to right'''
    x = list(str(n))
    for i in range(1, len(x)):
        y = x[i:]
        s = int(''.join(y))
        if is_prime(s):
            continue
        else:
            return False
    return True

def main():
    truncatable = []
    i = 10
    while len(truncatable) < 11:
        i += 1
        if is_prime(i):
            if trunc_left(i) == True and trunc_right(i) == True:
                truncatable.append(i)
            else:
                continue
        else:
            continue

    print("The sum of the truncatable primes is %s" %(sum(truncatable)))
    print("---%s seconds---" %(t.time()-start))

if __name__ == '__main__':
    main()
