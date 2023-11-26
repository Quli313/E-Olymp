n = int(input())
def bolen(n):
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            return i
        i += 1
    return n
print(bolen(n))
