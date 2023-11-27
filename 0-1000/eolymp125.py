h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())

baslangic = h1 * 3600 + m1 * 60 + s1
son = h2 * 3600 + m2 * 60 + s2
ferq_san = son - baslangic

saat = ferq_san // 3600
deq = (ferq_san % 3600) // 60
san = ferq_san % 60

print(f"{saat} {deq} {san}")
