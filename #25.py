import math
a = 0
for i in range(2941):
    b = math.gcd(35 * i, 205800)
    if math.sqrt(b) == int(math.sqrt(b)):
        a += 1
print(a)