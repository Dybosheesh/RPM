import math
a = int(input("a = 5"))
b = int(input("b = 6"))
c = int(input("c = 8"))
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
