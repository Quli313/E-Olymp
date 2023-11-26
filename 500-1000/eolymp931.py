n = int(input())
hasil = 1
cem = 0
for i in str(n):
    hasil*=int(i)
    cem+=int(i)
print(f"{(hasil/cem):.3f}")