a = int(input())
print("%s in Ottawa" % (a))
if a - 300 > 0:
    print("%s in Victoria" % (a - 300))
if a - 300 <= 0:
    print("%s in Victoria" % (a - 300 + 2400))

if a - 200 > 0:
    print("%s in Edmonton" % (a - 200))
if a - 200 <= 0:
    print("%s in Edmonton" % (a - 200 + 2400))

if a - 100 > 0:
    print("%s in Winnipeg" % (a - 100))
if a - 100 < 0:
    print("%s in Winnipeg" % (a - 100 + 2400))

print("%s in Toronto" % (a))
print("%s in Halifax" % (a + 100))
r = (a) + 130
r = str(r)
r.split()
u = int(r[1])
y = int(r[2])
st = int(r[0])
x = (u *10 + y)
if x >= 60:
    x = x - 60
    st += 1
    add = st * 100 + x
    print("%s in St. John's" %(add))
else:
    print("%s in St. John's" %(int(a)+130))
