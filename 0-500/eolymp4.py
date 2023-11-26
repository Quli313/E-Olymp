from math import sqrt

def noqteler(x1, y1, r1, x2, y2, r2):
    mesafe = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    if mesafe > r1 + r2 or mesafe < abs(r2 - r1):
        print( 0)
    elif mesafe == 0 and r1 == r2:
        print( -1)
    elif mesafe == r1 + r2 or mesafe == abs(r2 - r1):
        print( 1)
    elif mesafe < r1 + r2:
        print( 2)
    else:
        print( 0)

x1, y1, r1, x2, y2, r2 = map(int, input().split())
n = noqteler(x1, y1, r1, x2, y2, r2)
print(n)
