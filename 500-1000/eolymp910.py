n = int(input())
b = list(map(float, input().split()))
k = []
if len(b) == n:
    for i in b:
        if i>0:
            k.append(i)
    if len(k) > 0:
        print(f"{sum(k)/len(k):.2f}")
    else:
        print("Not Found")