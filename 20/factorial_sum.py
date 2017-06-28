import time

start_time = time.time()

#computes the factorial of n
def factorial(n):
  product = 1
  while n > 0:
    product *= n
    n -= 1
  return product

#computes the digit sum of a number
def digit_sum(n):
  summation = 0
  number = str(n)
  for i in number:
    summation += int(i)
  return summation

print(digit_sum(factorial(100)))
print("---%s seconds---" %(time.time() - start_time))
