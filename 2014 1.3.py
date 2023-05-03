a = int(input())
David = 100
Antonia = 100
for i in range(a):
    b = input()
    c = b.split()
    d = int(c[0])
    e = int(c[1])
    if (e) > (d):
        David = David - int(e)
    if (e) < (d):
        Antonia = Antonia - int(d)
    if e == d:
        David = David
        Antonia = Antonia
print(David)
print(Antonia)