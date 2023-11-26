d,p = map(float, input().split())
h = (p**2 - (d/2)**2)**0.5
s = d**2 + 2*d*h
H = (p**2 - (((2*(d**2))**0.5)/2)**2)**0.5
v = (1/3) * d**2 * H
print(f"{s:.3f} {v:.3f}")