n = int(input())
musbetler = []
en = list(map(int, input().split()))
if len(en) == n:
    for i in en:
        if i > 0:
            musbetler.append(i)
for j in range(n-1):
    uzun = list(map(int, input().split()))
    for z in uzun:
        if z>0:
            musbetler.append(z)
print(sum(musbetler))
#tek atdunha
#sa github
