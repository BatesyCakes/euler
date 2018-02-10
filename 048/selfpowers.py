import time as t

def self_power_sum(n):
    total = 0
    for i in range(1,n+1):
        total += (i**i)

    return total

def main():
    start = t.time()
    self_string = str(self_power_sum(1000))
    print(self_string[-10:])
    print("--- %s seconds---" %(t.time()-start))

if __name__ == '__main__':
    main()
