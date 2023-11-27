def funk(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def peter_ticket_passenger_skip(passenger_count, bilet_nömrəsi):
    if funk(bilet_nömrəsi):
        return 0
    
    for i in range(1, passenger_count):
        if funk(bilet_nömrəsi - i):
            return i

    return -1

sərnişin_say, bilet_nömrəsi = map(int, input().split())
netice = peter_ticket_passenger_skip(sərnişin_say, bilet_nömrəsi)
print(netice)
