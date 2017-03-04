result_list = []

tmp = 0

for x in range(2, 101):
    for y in range(2, 101):
        tmp = pow(x, y)
        result_list.append(tmp)

result = list(set(result_list))

print(len(result))
