from math import *

def triangular_generator(n):
  return (n*(n+1))/2

def pentagonal_generator(n):
  return (n*(3*n-1))/2

def hexagonal_generator(n):
  return n*(2*n-1)


def main():
  '''creates a set of approx. 100,000 triangular, pentagonal,
  and hexagonal numbers, then looks for a matching trio'''

  pentagonals = set(pentagonal_generator(n) for n in range(166,100000))

  triangulars = set(triangular_generator(n) for n in range(286,100000))

  hexagonals = set(hexagonal_generator(n) for n in range(144,100000))

  for t in triangulars:
    if t in pentagonals and t in hexagonals:
      print(t)


if __name__ == "__main__":
  main()
