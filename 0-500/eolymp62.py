n = int(input())
def faktorial_tapmaq(n):
    faktorial = 1
    for i in range(1, 2001):
        faktorial = faktorial * i
        if faktorial == n:
            return i
    return None

netice = faktorial_tapmaq(n)
if netice is not None:
    print(netice)
