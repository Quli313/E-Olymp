x = int(input())
if x < -4:
    print(x+5)
elif -4<=x<=7:
    print(x**2-3*x)
else:
    print(x**3+2*x)

#ikinci hell usulu
x = int(input())
result = (
    x + 5 if x < -4 else (
        x**2 - 3*x if -4 <= x <= 7 else (
            x**3 + 2*x
        )
    )
)
print(result)
