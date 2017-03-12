m = 0
for a in range(1, 100):
    for b in range(1, 100):
        m = max(m, sum(map(int, list(str(pow(a, b))))))
print(m)
