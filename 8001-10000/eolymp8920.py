
n = int(input())
def bolme(x):
    return x % 2 != 0 and x % 3 != 0 and x % 5 != 0

def tap(n):
    list = []
    num = 1

    while len(list) < n:
        if bolme(num):
            list.append(num)
        num += 1
    return list

print(*tap(n))
