n = int(input())
nstr = str(n)
k = []
for i in nstr:
    k.append(int(i))
print(f"{(sum(k))**0.5:.3f}")