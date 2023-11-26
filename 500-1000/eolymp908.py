n = int(input())
z = list(map(int, input().split()))
k=[]
if len(z) == n:
    for i in z:
        if i>0 and i%6==0:
            k.append(i)
    print(f"{len(k)} {sum(k)}")