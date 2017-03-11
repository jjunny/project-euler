from itertools import permutations


def calculation(max):
    checking = 1
    num = '0123456789'
    num_list = permutations(num)
    for x in num_list:
        if checking == max:
            return "".join(x)
        checking += 1

print(calculation(1000000))
