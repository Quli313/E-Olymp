n = int(input())
z=0
while z**3 < n:
    z+=1
for i in range(1,z):
    print(i**3, end=' ')