k = int(input())
n = int(input())
m = int(input())
d = int(input())


s = int((k*n*m*d) / (k*m*n - k*n - m*n - k*m ))

if s >= 1:
    print(s)
else: 
    print(-1)