a = int(input())
b = int(input())
c = 0
if a >= 1 and b >= 9:
    c+= 1
if a >= 2 and b >= 8:
    c+=1
if a >= 3 and b >= 7:
    c+=1
if a >=4 and b >= 6:
    c+=1
if a >= 5 and b >= 5:
    c+=1
if a >= 6 and b >= 4:
    c+=1
if a >= 7and b >= 3:
    c+=1
if a >= 8 and b >= 2:
    c+=1
if a >= 9 and b >= 1:
    c+=1
if c > 1 or c == 0:
    print("There are %s ways to get the sum 10."%(c))
if c == 1:
    print("There is 1 way to get the sum 10.")