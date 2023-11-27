n = int(input())
s = sorted(str(n))

a, b = 0, 0
for i in range(len(s)):
    a = a * 10 + int(s[i])
    b = b * 10 + int(s[-i - 1])

ferq = b - a
print('0' * (len(s) - len(str(ferq))) + str(ferq))
