
t100, t200 = map(float, input().split())
speed = 200 / (2 * (t200 - t100))
print("{:.6f}".format(speed))
