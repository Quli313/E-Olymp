n = int(input())
ededler = list(map(int, input().split()))
k = []

if len(ededler) == n:
    maxeded = max(ededler)
    mineded = min(ededler)

    for i in ededler:
        if i == maxeded:
            k.append(mineded)
        elif i == mineded:
            k.append(maxeded)
        else:
            k.append(i)

    print(*k)
