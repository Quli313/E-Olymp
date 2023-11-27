x1,y1,x2,y2,x3,y3 = map(float, input().split())

def sahe(x, y, z):
    s = (x + y + z) / 2
    return (s * (s - x) * (s - y) * (s - z)) ** 0.5
a = ((x2-x1)**2+(y2-y1)**2)**0.5
b = ((x3-x2)**2+(y3-y2)**2)**0.5
c = ((x1-x3)**2+(y1-y3)**2)**0.5
s1 = sahe(a, b, c)   
perimetr = a+b+c
#obaaaaaaaa

print(f'{perimetr:.4f} {s1:.4f}')
