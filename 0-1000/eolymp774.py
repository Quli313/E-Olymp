r, a, b = map(int, input().split())
if r**2 >= ((a**2)+(b**2))**0.5:
    print("YES")
else:
    print("NO")