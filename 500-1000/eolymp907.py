n = int(input())
k = list(map(float, input().split()))
eded=0
t=0
if len(k) == n:
    for i in k:
        t+=1
        if 0<i<=2.5:
            eded+=i
            break
    if eded>0:
        print(f"{t} {eded:.2f}")
    else:
        print("Not Found")
        ?