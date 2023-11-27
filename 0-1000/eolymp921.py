n = int(input())
z = list(map(float, input().split()))
k=[]
if len(z) == n:
    for i in z:
        if i<0:
            k.append(i)
    print(f"{len(k)} {sum(k):.2f}")