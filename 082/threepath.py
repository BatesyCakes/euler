import numpy as np
import time as t
start = t.time()

def min_path_sum(array):
    (rows, columns) = array.shape
    best = [array[row][0] for row in range(rows)]

    for col in range(1, columns):
        column = [array[row][col] for row in range(rows)]
        tmp = column[:]

        for i in range(columns):
            column[i] += best[i]

            for j in range(0, i): 
                if sum([best[j]]+tmp[j:i+1]) < column[i]:
                    column[i] = sum([best[j]]+tmp[j:i+1])

            for k in range(i, rows):
                if sum([best[k]] +tmp[i:k+1]) < column[i]:
                    column[i] = sum([best[k]] +tmp[i:k+1])

        best = column
    return min(best)

def main(file):
    array = np.genfromtxt(file, delimiter=",")

    print(min_path_sum(array))
    print("---%s seconds---" %(t.time()-start))

if __name__ == "__main__":
    main("matrix.txt")
