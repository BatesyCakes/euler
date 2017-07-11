import numpy as np
from time import time
start = time()

def max_path(triangle):
    rows = len(triangle)

    for i in reversed(range(rows - 1)):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


def main():
    triangle_file = open("triangle.txt")
    triangle_str = str((triangle_file).read())
    triangle = [[int(digit) for digit in line.strip().split()] for line in triangle_str.splitlines()]

    print(max_path(triangle))
    print("---%s seconds---" %(time() - start))

if __name__ == "__main__":
    main()
