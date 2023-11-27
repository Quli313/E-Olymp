#)))
a,b,c = map(int, input().split())
if 1 <= a and 1<=b and 1<=c and c <= a+b:
    print(a+b-c)
