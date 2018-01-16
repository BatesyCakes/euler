import time as t
start = t.time()

def digit_sum(n):
    lst = list(str(n))
    total = 0
    for i in lst:
        total += int(i)
    return total

def main():
    maximum = 0
    for a in range (90, 100):
        for b in range(90, 100):
            x = digit_sum(a**b)
            if x > maximum:
                maximum = x
    print("The maximum power digit sum is %s" %(maximum))
    print("---%s seconds---"%(t.time()-start))

if __name__ == "__main__":
    main()
