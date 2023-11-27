def sade(eded):
    if eded < 2:
        return False
    for i in range(2, int(eded ** 0.5) + 1):
        if eded % i == 0:
            return False
    return True

def novbeti(sade_eded):
    k = 0
    while not sade(sade_eded):
        sade_eded += 1
        k += 1
    return k

m, n = map(int,input().split())

adam = novbeti(n)

if m >= adam:
    print(adam+1)
else:
    print(adam)