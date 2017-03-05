lst = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
for x in range(0,20):
    a = input()
    lst[x] = a.split()

answer = []


def x_collector(x, y):
    return int(lst[x][y]) * int(lst[x + 1][y]) * int(lst[x + 2][y]) * int(lst[x + 3][y])


def y_collector(x, y):
    return int(lst[x][y]) * int(lst[x][y + 1]) * int(lst[x][y + 2]) * int(lst[x][y + 3])


def z_collector(x, y):
    return int(lst[x][y]) * int(lst[x + 1][y + 1]) * int(lst[x + 2][y + 2]) * int(lst[x + 3][y + 3])


def r_z_collector(x, y):
    return int(lst[x + 3][y]) * int(lst[x + 2][y + 1]) * int(lst[x + 1][y + 2]) * int(lst[x][y + 3])

for x in range(0, 17):
    for y in range(0, 17):
        answer.append(x_collector(x,y))
        answer.append(y_collector(x,y))
        answer.append(z_collector(x,y))
        answer.append(r_z_collector(x,y))

for x in range(17, 19):
    for y in range(0, 17):
        answer.append(y_collector(x,y))

for x in range(0, 17):
    for y in range(17, 19):
        answer.append(x_collector(x,y))

print(max(answer))
