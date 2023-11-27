def days_without_water(N):
    cumulative_water = 0
    days = 0

    for day in range(1, N + 1):
        cumulative_water += 1 / day
        if cumulative_water >= 0.5:
            break
        days += 1

    return N - days

N = int(input())
days = days_without_water(N)
print(days)
