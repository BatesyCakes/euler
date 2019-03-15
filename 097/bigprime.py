import time as t
start = t.time()


prime = 28433 * (2**7830457) + 1
result = prime % 10000000000

print("The last ten digits are %s" %(result))
print("--- %s seconds ---" %(t.time() - start))
