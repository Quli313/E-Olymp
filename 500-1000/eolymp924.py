from math import pi
s,r1 = map(float, input().split())
r2 = ((pi*(r1**2) - s)/pi)**0.5
print("{:.2f}".format(round(r2, 2)))