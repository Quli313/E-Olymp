n = int(input())
birinci = list(map(int, input().split()))

m = int(input())
ikinci = set(map(int, input().split()))

son = [elem for elem in birinci if elem not in ikinci]

print(len(son))
print(*son)
