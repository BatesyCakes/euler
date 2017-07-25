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

#brute force generation of the nth prime number
def primeGen(n):
  primes = []
  x = 2
  while len(primes) < n:
      if prime_check(x):
          primes.append(x)
      x += 1
  return primes[-1]
