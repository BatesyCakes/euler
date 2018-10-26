import time as t
start = t.time()
b = 85
n = 120
total = 10**12

while n < total:
  '''employs recursive solution to the differential equation 2b**2 - n**2 -2b - n = 0'''
  bNew = 3*b + 2*n -2
  nNew = 4*b + 3*n -3

  b = bNew
  n = nNew


print("There are %s blue discs out of %s total discs" %(b,n))
print("---%s seconds---" %(t.time()-start))
