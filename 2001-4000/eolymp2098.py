n = int(input())
k = list(map(int, input().split()))
if len(k) == n:
    print(*k[::-1])