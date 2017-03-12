from math import factorial

comb_list = []


def comb():
    f = factorial
    for x in range(23, 101):
        for y in range(1, x + 1):
            if f(x) / f(y) / f(x - y) >= 1000000:
                comb_list.append(f(x) / f(y) / f(x - y))

    print(len(comb_list))

comb()
