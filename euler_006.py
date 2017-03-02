def sum_of_squares():
    result_1 = 0
    for x in range(1, 101):
        result_1 += x ** 2
    return result_1


def square_of_consensus():
    result_2 = 0
    for y in range(1, 101):
        result_2 += y
    return result_2 ** 2

result = square_of_consensus() - sum_of_squares()
print(result)
