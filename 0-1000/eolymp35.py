n = int(input())

if n < 1:
    print(0)
    exit()

i = 1
a = 0

while a < n:
    a = 6 * i * i
    i += 1

i -= 1

def out(s):
    print(s)
    exit()

if i == 1:
    s = {1: 3, 2: 5, 3: 7, 4: 9, 5: 11, 6: 12}.get(n, 0)
    if s != 0:
        out(s)

s = 0
a = 12

for j in range(1, i):
    s += a
    a += 18

n = n - 6 * (i - 1) * (i - 1)

if n > 1:
    s += 2
    n -= 1

for j in range(1, i - 1):
    if n > 0:
        s += 2
        n -= 1
    if n == 0:
        break
    if n > 0:
        s += 1
        n -= 1
    if n == 0:
        break

for t in range(1, 6):
    if n > 0:
        s += 2
        n -= 1
    if n == 0:
        break
    for j in range(1, i):
        if n > 0:
            s += 2
            n -= 1
        if n == 0:
            break
        if n > 0:
            s += 1
            n -= 1
        if n == 0:
            break
    if n == 0:
        break

if n > 0:
    s += 2
    n -= 1

if n == 0:
    out(s)

if n > 0:
    s += 1
    n -= 1

if n == 0:
    out(s)
?