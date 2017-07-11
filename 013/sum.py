import numpy as np
from time import time
start = time()

def arraySum(array):
    large_sum = 0
    for n in array:
        large_sum += n
    large_sum = str(int(large_sum))
    return large_sum[0:10]

def main(file):
    array = np.genfromtxt(file, delimiter=" ")

    print(arraySum(array))
    print("---%s seconds---" %(time()-start))

if __name__ == "__main__":
    main("numbers.txt")
