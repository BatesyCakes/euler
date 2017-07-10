import time
import numpy as np
start = time.time()

def max_product(array):
    (rows, columns) = array.shape
    hproduct = 0
    vproduct = 0
    dproduct = 0

    #sweeps horizontal products
    for i in range(rows):
        for j in range(columns - 4):
            nhproduct = array[i,j] * array[i, j+1] * array[i, j+2] * array[i, j+3]
            if nhproduct > hproduct:
                hproduct = nhproduct
            else:
                continue

    #sweeps vertical products
    for i in range(rows - 4):
        for j in range(columns):
            nvproduct = array[i,j] * array [i-1, j] * array[i-2, j] * array[i-3, j]
            if nvproduct > vproduct:
                vproduct = nvproduct
            else:
                continue

    #sweeps diagonal products
    for i in range(rows - 4):
        for j in range(columns - 4):
            ndproduct = array[i,j] * array[i-1, j+1] * array[i-2, j+2] * array[i-3, j+3]
            if ndproduct > dproduct:
                dproduct = ndproduct
            else:
                continue

    return max(hproduct, vproduct, dproduct)

def main(file):
    array = np.genfromtxt(file, delimiter=" ")

    print(max_product(array))
    print("---%s seconds---" %(time.time()-start))

if __name__ == "__main__":
    main("grid.txt")
