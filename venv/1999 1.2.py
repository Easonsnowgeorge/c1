a = []
b = []
c = []
d = []
e = []
f = []
for i in range(1, 1001):
    if i % 3 == 2:
        a.append(i)
    aa = len(a)
for i in range(1, aa+1):
    if i % 3 == 2:
        b.append(a[i-1])
    bb = len(b)
for i in range(1, bb+1):
    if i % 3 == 2:
        c.append(b[i-1])
    cc = len(c)
for i in range(1, cc+1):
    if i % 3 == 2:
        d.append(c[i-1])
    dd = len(d)
for i in range(1, dd+1):
    if i % 3 == 2:
        e.append(d[i-1])
    ee = len(e)
for i in range(1, ee+1):
    if i % 3 == 2:
        f.append(e[i-1])
print(f)