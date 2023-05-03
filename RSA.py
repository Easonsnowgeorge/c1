a = int(input("smallest number"))
b = int(input("biggest number"))

def RSA(n):
    v = []
    for i in range(1, n+1):
        if n % i == 0:
            v.append(i)
    if len(v) == 4:
            return 0


count = 0
for n in range(a, b+1):
            if RSA(n) == 0:
                count += 1
print("The number of RSA numbers between %s and %s is %s"%(a, b, count))

