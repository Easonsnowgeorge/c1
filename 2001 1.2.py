a = int(input())
b = int(input())
c = 0
print(a)
print(b)
for i in range(1000):
    c+=1
    if (a * i) % b == 1:
        print(i)
        break
    if c == 1000:
        print("No such integer exists.")