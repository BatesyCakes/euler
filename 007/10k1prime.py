import math
import time
start_time = time.time()


# checks if a number is prime
def prime_check(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False;
    return x>1;

#brute force generation of the nth prime number
def prime_gen(n):
  primes = []
  x = 2
  while len(primes) < n:
      if prime_check(x):
          primes.append(x)
      x += 1
  return primes[-1]

print(prime_gen(10001))
print("--- %s seconds ---" %(time.time() - start_time))
