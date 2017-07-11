from time import time
start = time()

#Finds the longest collats sequence.
#SOptimized by skipping even starting numbers.
def largestChain(x):
    largest_chain = 0
    number = 0
    for n in range(3,x,2):
        chain = 1
        num = n
        while num != 1:
            if num % 2 == 0:
                num = num / 2
                chain += 1
            else:
                num = (3*num) + 1
                chain += 1
        if chain > largest_chain:
            largest_chain = chain
            number = n
    return number

print(largestChain(1000000))
print("---%s seconds---" %(time() - start))
