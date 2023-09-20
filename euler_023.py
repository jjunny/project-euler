def getdivisorsum(n):
    divisorslist = []
    for i in range(1, n):
        if n % i == 0:
            divisorslist.append(i)
    return sum(divisorslist)


abun = set()
for x in range(1, 28124):
    if getdivisorsum(x) > x:
        abun.add(x)

rst = set(range(28123))
for i in abun:
    for j in abun:
        if i + j in rst:
            rst.remove(i + j)

print(sum(rst))
