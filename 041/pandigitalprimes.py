import math
import time as t
start = t.time()

def is_pandigital(n):
    '''check if a number is pandigital'''
    x = sorted(str(n))
    for i in range(1, len(x) + 1):
        if x[i - 1] != str(i):
            return False
    return True

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

def main():
    for x in range(987654321, 1234567, -2):
        if is_pandigital(x):
            if is_prime(x):
                print(x)
                print("---%s seconds---" %(t.time()-start))
                break
            else:
                continue

if __name__ == "__main__":
    main()
