a, b, c = float(input()), float(input()), float(input())
from math import *

d = pow(b, 2) - 4 * a * c


if d == 0:
    print(-b / (2 * a))
elif d < 0:
    print("Нет корней")
elif d > 0:
    x1 = -b + d**0.5 / (2 * a)
    x2 = -b - d**0.5 / (2 * a)
    x1, x2 = min(x1, x2), max(x1, x2)
    print(((-b) - sqrt(d)) / (2 * a))
    print(((-b) + sqrt(d)) / (2 * a))
    print("fg")
