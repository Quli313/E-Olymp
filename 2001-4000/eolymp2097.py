a, b = map(int, input().split())

for i in range(a, b + 1):
    reqemler = set(str(i))
    if len(reqemler) == 3:
        print(i)
       
