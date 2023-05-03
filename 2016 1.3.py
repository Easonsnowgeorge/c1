n = input()
d = 0
for x in range(0, len(n)+1):
    for y in range(0, len(n)+1):
        p = n[x:y]
        if p == p[::-1]:
            z = len(p)
            if z>d:
                d = z
print(d)