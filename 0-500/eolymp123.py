def sifirlarinsayi(n):
    sifir = 0
    while n >= 5:
        n //= 5
        sifir += n
    return sifir

n = int(input())
son = sifirlarinsayi(n)
print(son)
