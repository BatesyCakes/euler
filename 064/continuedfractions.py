import math
import time as t
start = t.time()

'''This problem is solved using the iterative algorithm section of the wikipedia
page Methods on Computing Square Roots'''


result = 0
for n in range(2, 10001):
  a0 = math.floor(math.sqrt(n))
  root = math.sqrt(n)

  if a0 * a0 == n:
    continue
  else:
    period = 0
    d = 1
    m = 0
    a = a0

    while a != 2*a0:
      m = int((d * a) - m)
      d = int((n - (m * m)) / d)
      a = int((a0 + m) / d)
      period += 1

  if period % 2 == 1:
    result += 1

print("There are %s continued fractions that have an odd period" %(result))

print("--- %s seconds ---" %(t.time() - start))
