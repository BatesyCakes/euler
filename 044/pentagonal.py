from math import *


def pentagonal_generator(n):
  number = n
  pentagonal = (number*(3*number - 1))/2
  return pentagonal

'''
def is_pentagonal(x):
  n = (sqrt(24*x + 1) + 1)/6
  if n%2 == 0:
    return True
  else:
    return False
'''

def main():

  pentagonals = set(pentagonal_generator(n) for n in range(1,3000))

  for x in pentagonals:
    for y in pentagonals:
      if x+y in pentagonals and abs(x-y) in pentagonals:
        print(abs(x-y))


if __name__ == "__main__":
  main()
