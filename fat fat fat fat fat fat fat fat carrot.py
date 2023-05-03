a = 1
b = 0
c = 0
d = []
for i in range(10, 100):
    c = a + b
    if c % 2 == 0:
      d.append(c)
    if b == 9:
        b = 0
        a += 1
    b += 1

print(len(d))
