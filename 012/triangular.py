import math
from time import time
start = time()

#finds divisors of a number
def divisorGen(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.append(n)
    return list(set(divs))

#returns the nth triangular number
def triangleGen(n):
    triangular = 0
    for num in range(n + 1):
        triangular += num
    return triangular

def main():
    i = 1
    while len(divisorGen(triangleGen(i))) <= 500:
        i += 1
    print(triangleGen(i))
    print("---%s seconds---" %(time() - start))

if __name__ == "__main__":
    main()
