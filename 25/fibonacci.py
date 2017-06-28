import time
start_time = time.time()

a, b = 1, 1
index = 2
while len(str(b)) < 1000:
    a,b = b, a + b
    index += 1
print(index)
print('---%s second---' %(time.time() - start_time))
