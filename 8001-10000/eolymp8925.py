n = int(input())
def hasilleme(n):
    hasil = 1
    
    n_str = str(n)
    
    for i_str in n_str:
        i = int(i_str)
        
        if i % 2 != 0:
            hasil *= i
    
    if hasil == 0:
        return -1
    else:
        return hasil

print(hasilleme(n))
?