n = input()
a = "AEIOUY"
b = "aeiouy"
sait = 0

for herf in n:
    if herf in a or herf in b:
        sait += 1

print(sait)
