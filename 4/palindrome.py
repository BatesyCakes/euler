import time
start = time.time()

#finds the largest palindrome of two 3-digit products
pals = []
for i in range(900,1000):
  for j in range(900,1000):
    if str(i*j) == str(i*j)[::-1]:
      pals.append(i*j)

print(max(pals))
print("--- %s seconds ---" % (time.time() - start))
