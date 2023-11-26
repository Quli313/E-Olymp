def funksiya(k):
    list = []
    i = 2
    while i * i <= k:
        if k % i:
            i += 1
        else:
            k //= i
            list.append(i)
    if k > 1:
        list.append(k)
    return list

def enaz(k):
    esas_list = funksiya(k)
    son = 1
    for z in esas_list:
        son *= z
    return son


k = int(input())

print(enaz(k))
?