import time
from math import pow

start_time = time.time()
primes = []

for a in range(2,101):
    for b in range(2,101):
        primes.append(pow(a,b))
primeset = set(primes)

print(len(primeset))
print("---%s seconds---" %(time.time() - start_time))
