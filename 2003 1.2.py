import math
def perfet():
    for i in range(65000):
        a = int(input())
        if a == 0:
            break
        if math.sqrt(a) == i:
            print("Minimum perimeter is %s with dimensions %s x %s"% (int(4 * math.sqrt(a)), int(math.sqrt(a)), int(math.sqrt(a))))
        if math.sqrt(a) != i:
            b=[]
            for i in range(1, a+1):
                if a % i == 0:
                    b.append(i)
                    if len(b) % 2 == 1:
                        b.append(10)
            c = len(b)
            d = int(c/2)
            e = b[d]
            f = int(c/2 + 1)
            g = b[f-3]
            h = 2 * (e + g)
            print("Minimum perimeter is %s with dimensions %s x %s" %(h, e, g))
perfet()
