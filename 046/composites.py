import math
from itertools import product as product
from time import time as time
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


def main():
  primes = set()
  composites = set()
  squares = set(2*(n**2) for n in range(1,int(math.sqrt(10000))))

  for n in range(3,10000,2):
    if is_prime(n):
      primes.add(n)
    else:
      composites.add(n)

  sums = set(sum(x) for x in product(primes, squares))

  min_conjecture_destroyer = min(n for n in composites if n not in sums)

  print(min_conjecture_destroyer)
  print("--- %s seconds ---" %(time() - start_time))

if __name__ == "__main__":
  main()
