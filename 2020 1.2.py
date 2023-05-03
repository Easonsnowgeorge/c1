a = int(input())
b = int(input())
c = int(input())
d = 0
e = 0
f = 0
for i in range(100000000):
    d = c ** f * b
    e += d
    f += 1
    if b == 1 and c == 1:
        print(a)
        break
    if e > a:
        print(i)
        break