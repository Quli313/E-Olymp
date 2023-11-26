def obaaaaaaaa(x1, y1, x2, y2, x3, y3, x4, y4):
    s = 0.5 * abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1) - (y1 * x2 + y2 * x3 + y3 * x4 + y4 * x1))
    return round(s)

koor = list(map(int, input().split()))

x1, y1, x2, y2, x3, y3, x4, y4 = koor

print(obaaaaaaaa(x1, y1, x2, y2, x3, y3, x4, y4))
