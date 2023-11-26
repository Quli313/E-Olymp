import math
a, b, c = map(int, input().split())
d = b**2 - 4*a*c

if d < 0:
    print("No roots")
elif d == 0:
    root = -b / (2*a)
    print(f"One root: {int(root)}")
else:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Two roots: {int(min(root1, root2))} {int(max(root1, root2))}")
