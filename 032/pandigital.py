from time import time
start = time()

def pandigital_prods():
    pandigital = "123456789"
    pandigital_set = set()
    pandigital_list = []
    for i in range(100, 2000):
        for j in range(1, 2000):
            k = i*j
            string = str(i) + str(j) + str(k)
            length = len(string)
            if length < 9:
                continue
            elif length > 9:
                break
            elif length == 9:
                if sorted(string) == sorted(pandigital):
                    pandigital_set.add(k)
                else:
                    continue

    return sum(pandigital_set)

def main():
    print(pandigital_prods())
    print("---%s seconds" %(time() - start))

if __name__ == "__main__":
    main()
