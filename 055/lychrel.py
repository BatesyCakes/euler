def is_palindrome(x):
    return x == x[::-1]

def is_lychrel(n):
    num = str(n)
    iterations = 0
    done = False

    while not done:
        if iterations > 50:
            return True
        num = str(int(num) + int(num[::-1]))
        iterations += 1
        if is_palindrome(num):
            done = True
    return False

def main():
    count = 0
    for n in range(10,10000):
        if is_lychrel(n):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
