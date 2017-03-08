from sympy import factorint
from operator import mul
from functools import reduce

i = 10
while True:
    f = factorint(i*(i+1)/2)
    if reduce(mul, [f[k]+1 for k in f]) > 500:
        print(i*(i+1)/2)
        break
    i += 1
