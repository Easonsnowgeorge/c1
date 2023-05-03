a = int(input())
first = int(input())
second = int(input())
third = int(input())
num = 0
while a > 0:
    first += 1
    num += 1
    if first == 35:
        first = 0
        a += 30
    a = a - 1
while a > 0:
    second += 1
    num+=1
    if second == 100:
        second = 0
        a += 60
    a = a - 1
while a > 0:
    third +=1
    num += 1
    if third == 10:
        third = 0
        a += 9
    a = a - 1
print("Martha plays %s times before going broke."%num)