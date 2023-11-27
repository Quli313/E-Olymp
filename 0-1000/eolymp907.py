n = int(input())
setir = input()
massiv = list(map(float, setir.split(' ')))

for i in range(n):
    deyisen = massiv[i]
    if deyisen <= 2.5:
        print(f"{i + 1} {deyisen:.2f}")
        break

else:
    print("Not Found")
