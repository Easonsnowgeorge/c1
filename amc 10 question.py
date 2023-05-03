a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
h = 1
i = 1
total = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            for h in range(1, 10):
                                for i in range(1, 10):
                                    if(a != b and a != c and a != d and a != e and a != f and a != g and a != h and a != i and b != c and b != d and b != e and b != f and b != g and b != h and b != i and c != d and c != e and c != f and c != g and c != h and c != i and d != e and d != f and d != g and d != h and d != i and e != f and e != g and e != h and e != i and f != g and f != h and f != i and g != h and g != i and h != i and a *100 + b * 10 + c + d * 100 + e * 10 + f == g * 100 + h * 10 + i):
                                        total += 1
                                        print("%s%s%s + %s%s%s = %s%s%s" %(a,b,c,d,e,f,g,h,i))
print(total/2)


