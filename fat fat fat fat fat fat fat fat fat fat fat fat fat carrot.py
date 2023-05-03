a = 3*5*7
b = []
def nonprime(x):
    for i in range(2, x):
        if x%i == 0:
            return True

for i in range(1, a+1):
    if a % i == 0 and nonprime(i):
        b.append(i)

print(b)
