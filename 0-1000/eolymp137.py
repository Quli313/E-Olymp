n = int(input())
a,b = map(int, input().split())
def ebob(a, b):
    while b:
        a, b = b, a % b
    return a

print(ebob(a, b))
?