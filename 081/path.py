import numpy as np

file = open("matrix.txt")
string = file.read().replace('\n', ',').split(',')
del string[-1]
array = np.array(string).reshape(80,80)

print(array)
