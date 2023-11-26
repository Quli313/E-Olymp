from math import pi
R,r,h = map(float, input().split())
s = pi*(R+r) + (((h**2)+((R-r)**2))**0.5) + pi*(R**2) + pi*(r**2)
print(f"{s:.2f}")?