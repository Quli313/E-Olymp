n = int(input())
ededler = list(map(int, input().split()))
k = []

if len(ededler) == n:
    for i in ededler:
        if ededler.count(i) == 1:
            k.append(i)
    print(*k)