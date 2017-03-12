d1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
d2 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
d3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
d4 = ['hundred',' and', 'thousand']

l1 = [len(e) for e in d1]
l2 = [len(e) for e in d2]
l3 = [len(e) for e in d3]
l4 = [len(e) for e in d4]
# 1~99
s1 = sum(l1)*9 + sum(l2) + sum(l3)*10

# 1~99 101~199 ... 901~999
s2 = s1*10 + sum(l1)*99 + sum(l4[:2])*99*9

# 1~1000
s3 = s2 + sum(l1) + l4[0]*9 + l1[0] + l4[2]
print(s3)