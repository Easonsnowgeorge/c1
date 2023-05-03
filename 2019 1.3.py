x = int(input())
a=[]
for i in range(0,x):
    t=input()
    a.append(t)
for i in range(0,x):
    n=a[i]
    d=''
    p=0
    for i in range(0,len(n)):
        if i != len(n)-1 and n[i]==n[i+1]:
            p=p+1
        else:
            d = d+' '+str(p+1)+' '+n[i]
            p = 0
    print(d[1:len(d)])