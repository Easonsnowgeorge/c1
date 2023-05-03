b = input()
i=0.2/12
m=10
def pay(m):
    pb=b
    for n in range(12):
        pb=(pb-m)*(1+i)
    if pb>0:
        m+=10
        pay(m)
    else:
        print(m)
pay(m)



