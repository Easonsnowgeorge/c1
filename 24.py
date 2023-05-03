from collections import defaultdict
M=int(1e10+7)

def get_Prime(x):
    cnt=0
    for i in range(2,x+1):
        if i>x/i:break
        if x%i==0:
            cnt+=1
        while x%i==0:
            x/=i

    if x>1:cnt+=1
    print(cnt)

n=int(input())
primes,ans=defaultdict(int),1
for i in range(n):
    m=int(input())
    get_Prime(m)




