def minimize_ones_to_n(n):
    if n == 1:
        return 1

    operations = 0  
    expression = "1"  

    while expression.count("1") < n:
        expression += "+1"  
        operations += 1

    return operations


n = 119
min_operations = minimize_ones_to_n(n)
print(f"{n} sayısını minimum sayıda 1 kullanarak ifade etmek için gereken işlem sayısı: {min_operations}")
