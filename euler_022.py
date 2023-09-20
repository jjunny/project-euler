rst = 0
cnt = 1
with open("name.txt", "r") as f:
    word = f.read().replace('"','').split(",")
    word.sort()
    for w in word:
        tmp = 0
        for a in w:
            tmp += (ord(a)-64)
        rst += (tmp * cnt)
        cnt += 1
print(rst)
