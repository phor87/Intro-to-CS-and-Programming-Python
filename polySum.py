import math
def polysum(n, s):
    area = 0.25 * n * s ** 2 / math.tan(math.pi / n)
    perimeter = n * s
    return round(perimeter**2 + area, 4)

print(polysum(10, 67))