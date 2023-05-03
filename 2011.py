a = int(input())
b = int(input())
for i in range(100):
    c = a-b
    if c > b:
        d=c-b
    else:
        d = b-c
    if d > c:
        e = d-c
    else:
        e = c-d
    if e > d:
        f = e - d
    else:
        f = d - e

print(f)