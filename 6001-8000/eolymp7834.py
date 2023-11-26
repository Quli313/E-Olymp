n = int(input())
k = list(map(int, input().split()))
if len(k) == n:
    a = sorted(k, reverse=True)
    print(a[0] + a[1])