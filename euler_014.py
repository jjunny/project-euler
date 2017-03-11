collatz_counts = {}


def collatz(n):
    count = 1
    start = n
    while n != 1:
        if n in collatz_counts:
            count += collatz_counts[n]
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1

    collatz_counts[start] = count
    return count

answer = max(((collatz(i), i) for i in range(1, 1000000)))
print("The starting position generating the longest sequence is {0}".format(answer[1]))