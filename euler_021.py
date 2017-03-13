from sympy import divisors

d_nDic = {}
for i in range(3,10000):
    d_nDic[i] = sum(divisors(i))-i

ami = []
for i in d_nDic:
    if d_nDic[i] > 3 and d_nDic[i] < 10000:
        if i == d_nDic[d_nDic[i]] and i != d_nDic[i]:
            ami.append(i)

print(sum(ami))
