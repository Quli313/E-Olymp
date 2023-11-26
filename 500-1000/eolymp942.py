xa,ya = map(float, input().split())
xb,yb = map(float, input().split())
xc,yc = map(float, input().split())
xd,yd = map(float, input().split())
mesafe1 = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
mesafe2 = ((xb - xd) ** 2 + (yb - yd) ** 2) ** 0.5
print(f"{(xc+xa)/2:.3f} {(yc+ya)/2:.3f}")
print(f"{mesafe1:.3f} {mesafe2:.3f}")
