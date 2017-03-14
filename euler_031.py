c = [1, 2, 5, 10, 20, 50, 100, 200]
s = {i: 0 for i in range(1, 201)}
for i in c:
    s[i] += 1
    for j in range(i + 1, 201):
        s[j] += s[j - i]

print(s[200])
