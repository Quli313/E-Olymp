a, b, c, x, y = map(int, input().split())

if a <= x and b <= y or b <= x and a <= y:
    print("YES")
elif b <= x and c <= y or c <= x and b <= y:
    print("YES")
elif a <= x and c <= y or c <= x and a <= y:
    print("YES")
else:
    print("NO")
