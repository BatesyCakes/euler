def digit_sum(n):
  summation = 0
  number = str(n)
  for i in number:
    summation += int(i)
  return summation

d = 1
n = 2

for i in range(2,101):
  temp = d
  if i % 3 == 0:
    c = int(2 * (i / 3))
  else:
    c = 1
  d = n
  n = c * d + temp

print(digit_sum(n))
