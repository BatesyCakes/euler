import time
start_time = time.time()

names_file = open("names.txt")
names_text = names_file.read()
names = [name.strip('"') for name in names_text.split(',')]
names.sort()

#function that scores the name using ASCII values
def namescore(name):
	score=0
	for i in name:
		score += ord(i)-64
	return score

total=0
#iterates through names list and assigns index value to name and returns names value
for i in range(len(names)):
	total += namescore(names[i])*(i+1)
print(total)
print("---%s seconds---" %(time.time()-start_time))
