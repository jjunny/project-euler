i = 0
result = 0


def reverse_checker(n):
    n = str(n)
    reverse_n = n[::-1]

    if reverse_n == n:
        return True


hundreds = list(range(100, 1000))
tmp = []

for x in hundreds:
    for y in hundreds:
        number = x * y
        if reverse_checker(number) == True:
            tmp.append(number)

tmp.sort()
print(tmp.pop())
