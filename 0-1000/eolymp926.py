a, b, c, d, f = map(float, input().split())

def sahe(x, y, z):
    s = (x + y + z) / 2
    return (s * (s - x) * (s - y) * (s - z)) ** 0.5

s1 = sahe(a, b, f)   
s2 = sahe(c, d, f)  

cem = s1 + s2

print(f'{cem:.4f}')
