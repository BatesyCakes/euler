import time
start_time = time.time()


# checks if a number is prime
def prime_check(x):
    if x == 2 or x == 3:
        return True
    elif x % 2 == 0 or x < 2:
        return False
    for i in range(3,int(x**0.5)+1,2):   # only odd numbers
        if x % i==0:
            return False
    return True

#lists number rotations
def rotate(y):
    y = str(y)
    rotations = []
    iterations = len(y)
    while iterations > 0:
        y = y[1:len(y)] + y[0]
        rotations.append(int(y))
        iterations -= 1
    return rotations

primes = 1 #starts at 1 because 2 is a circular prime
#only iterate through odd numbers
for n in range(3,1000000,2):
    circular_prime = True
    for m in rotate(n):
        if not prime_check(m):
            circular_prime = False
            break
    if circular_prime:
        primes += 1

print(primes)
print("---%s seconds---" %(time.time() - start_time))
