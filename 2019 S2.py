from math import sqrt
def isprime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True
def solve(n):
    for i in range(2, n*2):
        if isprime(i) and isprime(n*2 - i):
            print(i, n*2 - i)
            break
n = int(input())
for i in range(n):
    a = int(input())
    solve(a)