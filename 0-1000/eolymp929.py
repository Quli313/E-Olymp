a, b, c, d = map(float, input().split())

if (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
    print("YES")
else:
    print("NO")
