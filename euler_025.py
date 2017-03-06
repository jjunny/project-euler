a = 1
b = 1
x = 1
while True:
    if len(str(a)) >= 1000:
        break
    a, b = b, a + b
    x += 1

print(x)
