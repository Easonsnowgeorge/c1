N = int(input())
boxes = []
items = []
boxesx = []
boxesy = []
boxesz = []
for i in range(N):
    x, y, z = input().split()
    boxesx.append(x)
    boxesy.append(y)
    boxesz.append(z)
    boxes.append(int(x) * int(y) * int(z))
itemsx = []
itemsy = []
itemsz = []
M = int(input())
for i in range(M):
    x, y, z = input().split()
    itemsx.append(x)
    itemsy.append(y)
    itemsz.append(z)
    items.append(int(x) * int(y) * int(z))

for i in range(len(items)):
    boxed = False
    for j in range(len(boxes)):
        if items[i] <= boxes[j]:
            if itemsx[i] <= boxesx[j] or itemsx[i] <= boxesy[j] or itemsx[i] <= boxesz[j]:
                if itemsx[i] <= boxesx[j] and itemsx[i] <= boxesy[j] and itemsx[i] <= boxesz[j]:
                    volume = boxes[j]
                    boxed = True
                    break
        else:
            boxed = False
    if boxed == False:
        print("Item does not fit.")