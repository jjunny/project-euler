def isprime(n, primes):
    for p in primes:
        if n % p == 0: return False
        if p*p > n: return True

primes = [2]
n, cnt = 3, 1
while cnt < 10001:
    if isprime(n, primes):
        primes.append(n)
        cnt += 1
    n += 2

print(primes[-1])

# 베낀 코드