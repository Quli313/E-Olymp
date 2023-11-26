n = int(input())
k=0
for i in range(n):
    x,y = map(float, input().split())
    if y < 50:
        k+=x
print(int(k))