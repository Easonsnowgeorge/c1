a=input()
a=a.split()
x=int(a[0])
y=int(a[1])
z=int(a[2])
s=input()
no=0
v=["a","e","i","o","u","y"]
vn=0
c="bcdfghjklmnpqrstvwxyz"
cn=0

for i in range(x-z):
    if s[i] in v:
        for j in range(1,z+1):
            if s[i+j] not in v:
                break
            if s[i+j] in v :
                vn+=1
        if vn>z:
            no=1
            break
for i in range(x-y):
    if s[i] in c:
        for j in range(1,y+1):
            if s[i+j] not in c :
                break
            if s[i+j] in c:
                cn+=1
        if cn>y:
            no=1
            break
if no==0:
    print("YES")
if no==1:
    print("NO")