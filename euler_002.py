list = []
result = []

a = 0
b = 1
while a <= 4000000:
    list.append(a)
    tmp_b = b
    b = tmp_b + a
    a = tmp_b

for x in list:
    if x % 2 == 0:
        result.append(x)

print(sum(result))
