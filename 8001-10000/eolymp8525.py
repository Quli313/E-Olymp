n = int(input())
matrix = []
for i in range(n):
    setir = list(map(int, input().split()))
    matrix.append(setir)

say = 0
cem = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] < 0 and matrix[i][j] % 2 == 0:
            say += 1
            cem += matrix[i][j]

print(say, cem)
