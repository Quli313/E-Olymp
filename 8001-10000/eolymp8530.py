n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())


for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()
