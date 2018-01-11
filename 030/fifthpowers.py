import time as t
start = t.time()

def is_narcissistic(n):
    '''determines if a number is narcissistic or pseudo-narcissistic'''
    x = str(n)
    lst = list(x)
    power_sum = 0
    for i in lst:
        y = int(i)
        power_sum += y**5
    if power_sum == n:
        return True
    return False

def main():
    narcs = []
    for x in range(2, 400000):
        if is_narcissistic(x):
            narcs.append(x)
        else:
            continue
    print("The sum is %s" %(sum(narcs)))
    print("---%s seconds---" %(t.time() - start))

if __name__ == "__main__":
    main()
