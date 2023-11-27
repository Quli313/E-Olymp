import math
k = int(input())
ededler = list(map(int, input().split()))
if k == len(ededler):

    def ekob_tap(a, b):
        return a * b // math.gcd(a, b)

    def n_ekob(ededler):
        ekob = ededler[0]
        for eded in ededler[1:]:
            ekob = ekob_tap(ekob, eded)
        return ekob


    ekob = n_ekob(ededler)

    print(ekob)
