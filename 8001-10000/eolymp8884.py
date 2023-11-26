def tip(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return "equilateral"
        elif a == b or a == c or b == c:
            return "isosceles"
        else:
            return "versatile"
    else:
        return "invalid"

a, b, c = map(int, input().split())

print(tip(a, b, c))
