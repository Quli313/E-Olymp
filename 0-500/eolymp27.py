n = int(input())
def dovrutap(n):
    ikilik_str = bin(n)[2:]  #
    max_surus = n

    for i in range(1, len(ikilik_str)):
        ikilik_str = ikilik_str[1:] + ikilik_str[0]
        nums = int(ikilik_str, 2)  
        max_surus = max_surus(max_surus, nums)

    return max_surus

max_surus_qiymet = dovrutap(n)
print(max_surus_qiymet)
