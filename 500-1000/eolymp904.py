n = int(input())
ededler = list(map(int, input().split()))
k = []
if len(ededler) == n:
    for i in ededler:
        if i>=0:
            k.append(i+2)
        else:
            k.append(i)
    print(*k)