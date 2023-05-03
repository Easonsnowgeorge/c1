n=int(input())
ne=[-1]
noloop=[0]*1000
for i in range(n):
    ne.append(int(input()))

for i in range(1,n+1):
    if ne[i]==0:
        noloop[i]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        if noloop[ne[j]]==1:
            noloop[j]=1

print(sum(noloop))