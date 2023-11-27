k = []
while True:
    n = int(input())
    if n % 2 == 0:
        k.append(n)
    if n == 0:
        break

print(sum(k))
