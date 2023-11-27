m, n = map(int, input().split())

def fakt(x):
    if x == 0 or x == 1 or x<0:
        return 1
    else:
        return x * fakt(x - 1)

son = fakt(n) // (fakt(m) * fakt(n - m))
print(son)
