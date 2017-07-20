from time import time
start = time()

#tests wether a number is abundant or not
def isAbundant(n):
    div_sum = 0
    for i in range(1, int((n/2 + 1))):
        if n % i == 0:
            div_sum += i

    if div_sum > n:
        return True
    else:
        return False

def main():
    abundants = []
    abund_sums = set()
    abundants_sum = 0
    total = 0

    #checks if a number is abundant and adds to list
    for i in range(1, 28123):
        if isAbundant(i):
            abundants.append(i)

    #adds abundants sums under 28123 to a set
    for x in abundants:
        for y in abundants:
            z = x + y
            if z < 28123:
                abund_sums.add(z)
            else:
                break

    #sums every number under 28123 that is not and abundants sum
    for j in range(1, 28123):
        if j not in abund_sums:
            total += j

    print(total)
    print("---%s seconds" %(time() - start))

if __name__ == '__main__':
    main()
