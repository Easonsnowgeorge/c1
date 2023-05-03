a = 0
x = int(input("enter a number"))
for i in range(3,x+1):
    a += i*(i-1)*(i-2)
print(a)