import time as t

def is_89chain(n):
    while n != 1 and n != 89:
        num = 0
        n = str(n)
        for digit in n:
            num += int(digit)**2
        n = num
    if n == 89:
        return True
    elif n == 1:
        return False

def main():
    start = t.time()
    eight_nine = 0
    for number in range(1,10000001):
        if is_89chain(number):
            eight_nine += 1
    print('%s numbers chain to 89' %(eight_nine))
    print('--- %s seconds---' %(t.time()-start))

if __name__ == '__main__':
    main()
