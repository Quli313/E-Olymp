a, b, c = map(int, input().split())

if a + b > c and a + c > b and b + c > a:
    if a == b or a == c or b == c:
        print(a + b + c)
    else:
        print("No")
else:
    print("No")
