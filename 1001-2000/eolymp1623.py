a,b,c = map(int, input().split())
if a%2==0 and b%2!=0 or a%2!=0 and b%2==0 or c%2==0 and b%2!=0 or b%2==0 and c%2!=0 or a%2==0 and c%2!=0 or c%2==0 and a%2!=0:
    print("YES")
else:
    print('NO')