n = int(input())

def f91(n):
    if n <= 100:
        return f91(f91(n + 11))
    else:
        return n - 10

result = f91(n)
print(result)
