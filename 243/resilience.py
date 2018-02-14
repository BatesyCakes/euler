from fractions import gcd
from fractions import Fraction


def resilients(den):
  '''Returns the total number of resilient numerators.'''
  total = 0

  for num in range(1,den):
    if gcd(num,den) == 1:
      total += 1
    else:
      continue

  return total


check = 94744

while Fraction(resilients(check),(check-1)) >= Fraction('15499/94744'):
  check += 1

print(check)
