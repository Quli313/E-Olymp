import math

def find_surface_area(b, alpha):
    alpha_rad = math.radians(alpha)
    l = b / math.cos(alpha_rad)
    base_area = b**2
    sahe = 2 * b * l
    cemsahe = base_area + sahe
    return round(cemsahe, 3)

b, alpha = map(int, input().split())
result = find_surface_area(b, alpha)
print(result)?
