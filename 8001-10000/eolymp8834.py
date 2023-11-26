x,y = map(float, input().split())
print(f"{(((2*x*y)/((x**2+y**2)**0.5))-((((x+y-1)**2)/(x*y)))):.3f}")