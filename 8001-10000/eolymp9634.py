

n = int(input())
for i in range(n):
    x,y = map(str, input().split())
    if float(x) >= 3.5 and y in ['A','B']:
        print(1)
    else:
        print(0)
