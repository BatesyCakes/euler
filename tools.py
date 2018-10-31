import math


def divisor_gen(n):
    '''generates list of divisors of a number'''
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.append(n)
    return list(set(divs))


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


def digit_sum(n):
    '''sums the digits of a given number'''
  summation = 0
  number = str(n)
  for i in number:
    summation += int(i)
  return summation


def is_pandigital(n):
    '''check if a number is pandigital'''
    x = sorted(str(n))
    for i in range(1, len(x) + 1):
        if x[i - 1] != str(i):
            return False
    return True

def pascals_triangle(n):
    '''returns pascals triangle up to n rows'''
    rows = [[1]]
    for _ in range(1, n+1):
        rows.append([1] +
                    [sum(pair) for pair in zip(rows[-1], rows[-1][1:])] +
                    [1])
    return rows

def pascals_row(n):
    '''generates the nth row of Pascal's triangle. The first row is n=0'''
  row = [1]
  if n > 0:
    for i in range(1,n+1):
      num = row[i-1] * (n + 1 - i)/i
      row.append(num)
    return row
  else:
    return row

def numberToBase(n, b):
    '''converts integer n to any base b'''
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]
