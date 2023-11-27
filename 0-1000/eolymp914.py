n = int(input())
k = list(map(float, input().split()))

if n == len(k):
    t = [abs(x) for x in k]
    son = max(t)
    print(f"{son:.2f}")
