fibs = [1,1]
total = 0

while fibs[-1] < 4000000:
  if fibs[-1] % 2 == 0:
    total += fibs[-1]
  fibs.append(fibs[-1] + fibs[-2])
    
print(total)