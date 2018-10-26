#Solution using Lucas's Theorem
total = 1

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b)+1)
        n //= b
    return digits[::-1]


for n in range(1, 10**9):
  product = 1
  string = numberToBase(n, 7)
  for digit in string:
    product *= digit
  total += product

print (total)
