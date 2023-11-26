n = int(input())
def bolen(n):
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            return i
    return 1

print(bolen(n))
?