import time
start = time.time()

sums = 0
for x in range(1000000):
    if str(x) == str(x)[::-1] and str(bin(x))[2:] == str(bin(x))[:1:-1]:
        sums += x

print(sums)
