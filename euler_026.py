def ncycle(n):
    m, s = 1, set()
    while True:
        if n > m:
            if m in s:
                if m == 0: return 0
                else: return len(s)
            s.add(m)
            m *= 10
        else: m %= n

for n in range(997, 499, -2):
    if ncycle(n) == n-1:
        print(n)
        break
