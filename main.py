import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = ((b ** 2) - (4 * a * c))

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x1 = -b / (2 * a)
    print(x1)
elif D < 0:
    print("No")
else:
    print("impossible")
