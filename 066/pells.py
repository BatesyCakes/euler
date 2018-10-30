import math
import time as t
start = t.time()

'''Solution to Pell's equation using the continued fractions method
used in Project Euler 064'''

maximum = 0
answer = 0

for D in range(2, 1001):
  a0 = int(math.sqrt(D))

  if a0*a0 == D:
    continue
  else:
    d = 1
    m = 0
    a = a0

    x1 = 1 #x_(i-1)
    y1 = 0 #y_(i-1)
    x = a0 #x_i
    y = 1  #y_i

    while (x*x - D*y*y != 1):
      m = int((d * a) - m)
      d = int((D - (m * m)) / d)
      a = int((a0 + m) / d)

      x2 = x1 #x_(i-2)
      x1 = x
      y2 = y1 #y(i-2)
      y1 = y

      x = a*x1 + x2
      y = a*y1 + y2

    if x > maximum:
      maximum = x
      answer = D

print("The largest x is obtained when D = %s" %(answer))
print("--- %s seconds" %(t.time()-start))
