import math

#generates list of divisors of a number
def divisorGen(n):
    divs = [1]
    for i in xrange(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.append(n)
    return list(set(divs))


# checks if a number is prime
def isPrime(n):
    for i in range(2, int(math.sqrt(x)+1)):
        if n % i == 0:
            return False;
    return n>1;

#brute force generation of the nth prime number
def primeGen(n):
  primes = []
  x = 2
  while len(primes) < n:
      if prime_check(x):
          primes.append(x)
      x += 1
  return primes[-1]
