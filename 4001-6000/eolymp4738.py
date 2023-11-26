n = int(input())
k = list(map(int,input().split()))
print(*sorted(k,reverse=True))