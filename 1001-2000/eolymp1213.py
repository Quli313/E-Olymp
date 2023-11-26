input_str = input()

ededler = input_str.split()

a, b = map(int, ededler[0].split('^'))

c, d = map(int, ededler[1].split('^'))

if a**b > c**d:
    print(f"{a}^{b}")
else:
    print(f"{c}^{d}")
