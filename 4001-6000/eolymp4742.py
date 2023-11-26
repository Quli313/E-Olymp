import math

n = int(input())
t = 0

for i in range(2, math.isqrt(n) + 1):
    if n % i == 0:
        t += 2 if i * i != n else 1

print(t)
