from time import time
start = time()

def is_pandigital():
    pandigital = "123456789"
    pandigital_list = []

    for i in range(10000):
        string = ""
        for j in range(1,7):
            if len(string) < 9:
                string += str(i * j)
            elif len(string) == 9:
                if sorted(string) == sorted(pandigital):
                    pandigital_list.append(string)
                else:
                    break
            else:
                break

    return max(pandigital_list)
def main():
    print(is_pandigital())
    print("---%s seconds" %(time() - start))

if __name__ == "__main__":
    main()
