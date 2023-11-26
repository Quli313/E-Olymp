from collections import Counter
n = int(input())
z = []
for i in range(n):
    k = input()
    z.append(k)

def tekrar(x):
    say = Counter(x)
    
    encox = max(say.values())
    
    tekrarlar = [i for i, frekans in say.items() if frekans == encox]
    
    return tekrarlar

print(*tekrar(z)[-1::], z.count(tekrar(z)[0]))


?????
?
