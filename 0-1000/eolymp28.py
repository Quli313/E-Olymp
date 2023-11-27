import random

a = int(input())

def fakt(x):
    son = 1
    for i in range(1, x + 1):  
        son *= i
    return son

while True:  
    n = random.randint(1, 100)
    m = random.randint(1, n)
    if n-m > 1 and m > 1 and n != m and fakt(n) / fakt(n-m) == a:
        print(m,n)
        break
