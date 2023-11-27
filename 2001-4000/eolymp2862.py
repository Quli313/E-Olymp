def f(n):
    say = 0
    for i in range(1, n + 1):
        if n % i == 0:
            say += 1
    return say

n = int(input())
print(f(n))
