n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:2}", end=" ") # :2 (iki reqemlik yer oldugunu bildirir ve daha duzgun, seliqeli yazilir)
    print()
