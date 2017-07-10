import time as t
from math import factorial
start = t.time()

#counts indistinct cominatoric values of n,r that exceed one million
def combinatoric_counter(i):
    count = 0

    for n in range(i+1):
        for r in range(n+1):
                dif = n - r
                if (factorial(n))/(factorial(r)*factorial(dif)) > 1000000:
                    count += 1
    return count

def main():
    print(combinatoric_counter(100))
    print("---%s seconds---" %(t.time() - start))

if __name__ == "__main__":
    main()
