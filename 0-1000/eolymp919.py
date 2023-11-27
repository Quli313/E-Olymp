n = int(input())
k = list(map(float, input().split()))

cem = 0
say = 0

for i in range(1, n + 1):
    if i % 3 == 0 and k[i - 1] > 0:
        cem += k[i - 1]
        say += 1

print(f"{say} {cem:.2f}")
