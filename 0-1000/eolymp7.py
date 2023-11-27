def rum_ereb(rum):
    rum_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prev_value = 0

    for numeral in reversed(rum):
        value = rum_dict[numeral]
        if value < prev_value:
            integer -= value
        else:
            integer += value
        prev_value = value

    return integer

def integer_to_rum(integer):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    rum = ''
    i = 0
    while integer > 0:
        for _ in range(integer // val[i]):
            rum += syb[i]
            integer -= val[i]
        i += 1
    return rum

def add_rum_numerals(expression):
    parts = expression.split("+")
    int_parts = [rum_ereb(part) for part in parts]
    result = sum(int_parts)
    return integer_to_rum(result)

expression = input()
result = add_rum_numerals(expression)
print(result)
