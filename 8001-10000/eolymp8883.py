a, b, c, d = map(int, input().split())

if (a + b == c + d or a + c == b + d or a + d == b + c) and (a<=0 and b <=0 and c<=0 and d<=0):
    print(a + b + c + d)
else:
    print("No")
?