m, n, k = map(int, input().split())
print(m // n, end='.')
d = m % n
for i in range(k):
    d *= 10
    print(d // n, end='')
    d %= n