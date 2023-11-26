a = int(input())
def sade(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if sade(a):
    print(1)
else:
    print(0)