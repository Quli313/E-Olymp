n = int(input())
k = list(map(float, input().split()))
if len(k) == n:
    print(f"{sum(k):.1f}")