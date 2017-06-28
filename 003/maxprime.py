def max_prime(num):
    x = 2
    while x^2 <= num:
        while num % x == 0:
            num /= x
        x += 1
    if (num > 1):
        return num
    return x
    
    
print(max_prime(600851475143))