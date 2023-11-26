def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1) * 2 + n

def g(k):
    cem = 0
    t = 1
    
    while cem <= k:
        cem += f(t)
        t += 1

    return t

k = int(input())
print(g(k))
?