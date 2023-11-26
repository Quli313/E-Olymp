n = int(input())
yaslar = list(map(int, input().split()))

say = {}

for i in yaslar:
    if i in say:
        say[i] += 1
    else:
        say[i] = 1

encox = max(say, key=say.get)
print(encox)
