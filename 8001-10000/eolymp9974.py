n = int(input())
k=0
for i in range(1,n+1):
    k += 3**(i-1)
    i+=1
print(k)
    