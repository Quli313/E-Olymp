n = int(input())
i = 2
k = []
while i <= n:
    if n % i == 0:
        k.append(i)
        n //= i
    else:
        i += 1
print(*k)?