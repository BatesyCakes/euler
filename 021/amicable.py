import math
import time as t
start = t.time()

def divisor_gen(n):
    '''generates list of proper divisors of a number'''
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    return list(set(divs))

def amicable_sum(limit):
    '''generates sum of amicable numbers up to specified limit.'''
    amicables = set()

    for a in range(2, limit + 1):
        sum_adiv = sum(divisor_gen(a))
        sum_bdiv = sum(divisor_gen(sum_adiv))
        if a == sum_bdiv and a != sum_adiv:
            amicables.add(a)
            amicables.add(sum_bdiv)

    return sum(amicables)


print(amicable_sum(10000))
print("---%s seconds---" %(t.time()-start))
