n = input()

def reqemtap(x):
    tekyer = 0
    cutyer = 0

    for index, reqem in enumerate(x, start=1):
        if index % 2 == 0:
            cutyer += int(reqem)
        else:
            tekyer += int(reqem)
    
    son = cutyer * tekyer
    return son

son = reqemtap(n)

print(son)
