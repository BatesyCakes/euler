import math
import time
start_time = time.time()


# checks if a number is prime
def prime_check(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False;
    return x>1;

#sums all of the prime number below n
def primes_sum(n):
  prime_sum = 0
  x = 2
  while x < n:
      if prime_check(x):
          prime_sum += x
      x += 1
  return prime_sum

print(primes_sum(2e6))
print("--- %s seconds ---" %(time.time() - start_time))
