n = int(input())
def cemleme(n):
    cem = 0
    
    n_str = str(abs(n))
    
    for i_str in n_str:
        i = int(i_str)
        
        if i % 2 == 0:
            cem += i
    
    if cem == 0:
        return -1
    else:
        return cem

print(cemleme(n))
?