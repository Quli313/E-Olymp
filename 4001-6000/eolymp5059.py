n = int(input())
k = list(map(int, input().split()))

while len(str(k)) <= len(str(n)):
    min1 = min(k)
    k.remove(min1)
    min2 = min(k)

    print(min1, min2)

    n = int(input())
    k = list(map(int, input().split()))
?