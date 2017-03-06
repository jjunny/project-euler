from functools import reduce
from operator import mul


def d(n):
    sz = 0
    while n > (sz+1)*9*pow(10, sz):
        n -= (sz+1)*9*pow(10, sz)
        sz += 1
    L, d = divmod((n-1), sz+1)
    return int(str(pow(10, sz)+L)[d])

print(reduce(mul, (d(10**i) for i in range(7))))
