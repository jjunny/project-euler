

def chk_pn(n, pn):
    for p in pn:
        if n % p == 0:
            return False
        if p**2 > n:
            return True


def inc_pn(pn):
    n = pn[-1] + 2
    while True:
        if chk_pn(n, pn):
            pn.append(n)
            return pn
        n += 2


def factor(n, pn):
    # n > 2
    i, fDic = 0, {}
    while True:
        p = pn[i]
        if p == pn[-1]:
            pn = inc_pn(pn)
        if n % p == 0:
            if p in fDic:
                fDic[p] += 1
            else:
                fDic[p] = 1
            n /= p
            i -= 1
        i += 1
        if pn[i]**2 > n:
            if n in fDic:
                fDic[n] += 1
            else:
                fDic[n] = 1
            return fDic

pn, SCM = [2, 3], {}
for i in range(4, 21):
    fDic = factor(i, pn)
    for k in fDic:
        if k in SCM:
            SCM[k] = max(SCM[k], fDic[k])
        else:
            SCM[k] = fDic[k]

op = 1
for x in SCM:
    op *= x**SCM[x]

print(op)

# 베낀 코드