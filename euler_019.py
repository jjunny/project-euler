d = 2 # Monday - 1 Jan 1901
c = 0
for year in range(1901,2001):
    for mon in range(1,13):
        if d == 0: c += 1
        if mon in (1, 3, 5, 7, 8, 10, 12): d = (d + 3) % 7
        elif mon in (4, 6, 9, 11): d = (d + 2) % 7
        elif year % 4 == 0: d = (d + 1) % 7

print(c)
