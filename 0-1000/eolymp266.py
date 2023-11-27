def muqayise(x, y):
    if len(x) > len(y):
        return ">"
    elif len(x) < len(y):
        return "<"
    elif len(x) == len(y):
        for i in range(len(x)):
            if x[i] != y[i]:
                if x[i] > y[i]:
                    return ">"
                return "<"
    return "="

def main():
    a = input().lstrip('0')
    if a == "":
        a = "0"
    b = input().lstrip('0')
    if b == "":
        b = "0"
    print(muqayise(a, b))
?
