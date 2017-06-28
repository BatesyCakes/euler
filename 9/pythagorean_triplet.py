import time
start_time=time.time()

for a in range(500):
  for b in range(a,500):
    for c in range(b,500):
      if a*a + b*b == c*c and a+b+c==1000:
        print(a*b*c)
print("---%s seconds ---" %(time.time() - start_time))
