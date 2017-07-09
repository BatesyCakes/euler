import numpy as np
import time as t
start = t.time()

def min_path_sum(array):
    (rows, columns) = array.shape

    for i in range(1,columns):
        array[0, i] += array[0, i-1]
    for i in range(1,rows):
        array[i, 0] += array[i-1, 0]

    for i in range(1, rows):
        for j in range(1, columns):
            array[i,j] += min(array[i - 1, j], array[i, j - 1])
    return array[row-1,column-1]

def main(file):
    array = np.genfromtxt(file, delimiter=",")

    print(min_path_sum(array))
    print("---%s seconds---" %(t.time()-start))

if __name__ == "__main__":
    main("matrix.txt")
