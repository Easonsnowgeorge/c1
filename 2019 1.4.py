a = input()
b = ['1', '2', '3', '4']
for i in range(len(a)):
    if a[i] == 'H':
        b[0], b[2] = b[2], b[0]
        b[1], b[3] = b[3], b[1]
    if a[i] == 'V':
        b[0], b[1] = b[1], b[0]
        b[2], b[3] = b[3], b[2]
print(b[0], b[1])
print(b[2], b[3])