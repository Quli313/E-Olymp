n = int(input())
k = []
for i in range(n):
    l = int(input())
    k.append(l)
print(*(k[::-1]))