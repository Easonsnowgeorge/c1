a = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
b = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
money = int(input())
for i in range(money):
    z = int(input())
    b.remove(a[z-1])
offer = int(input())
average = sum(b)/(10-money)
if average > offer :
    print("no deal")
else:
    print("deal")