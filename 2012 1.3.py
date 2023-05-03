
a = int(input())
star = ""
x = ""
space = ""
for i in range(a):
    star = star + "*"
    x = x + "x"
    space = space + " "
for i in range (a):
    print(star+x+star)
for i in range (a):
    print(space+x+x)
for i in range (a):
    print(star+space+star)
