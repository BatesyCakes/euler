import time as t
start = t.time()

def main():
    '''function that concatenates loop into Champernowne's constant'''
    c = ""
    d = []
    for x in range(1,1000001):
        s = str(x)
        c += s
    for digit in c:
        d.append(int(digit))
    print(d[0] * d[9] * d[99] * d[999] * d[9999] * d[99999] * d[999999])
    print("---%s seconds---" %(t.time()-start))

if __name__ == "__main__":
    main()
