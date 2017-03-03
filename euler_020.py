digit_list = []

tmp = 1

result = 0

for x in range(1, 101):
    tmp *= x

tmp = str(int(tmp))

digit_list += tmp

for y in digit_list:
    result += int(y)

print(result)
print(digit_list)
