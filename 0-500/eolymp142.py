def f(x1, y1, x2, y2, x3, y3):
    if (y1 - y2) * (x3 - x2) == (y3 - y2) * (x1 - x2):
        if min(x2, x3) <= x1 <= max(x2, x3) and min(y2, y3) <= y1 <= max(y2, y3):
            return 1  
    return 0  

x1, y1, x2, y2, x3, y3 = map(int, input().split())
print(f(x1, y1, x2, y2, x3, y3))
