from math import factorial
import time as t
start = t.time()

def main():
    '''Finds the sum off all factorions (exluding 1 and 2).'''

    factorions = []
    for x in range(10,50001):
        fac_sum = 0
        s = str(x)
        for digit in s:
          num = int(digit)
          fac_sum += factorial(num)

        if fac_sum == x:
          factorions.append(x)

    print(sum(factorions))
    print("---%s seconds---" %(t.time()-start))

if __name__ == "__main__":
    main()
