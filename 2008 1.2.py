l = []
lista = []
list = ['A', 'B', 'C', 'D', 'E']
for i in range(101):
    a = int(input())
    b = int(input())
    l.append(a)
    l.append(b)
    if a == 4:
        break
    for i in range(b):
        if a == 1:
            list = list[1:] + list[:1]
        if a == 2:
            list = list[4:] + list[:4]
        if a == 3:
            lista.append(list[0])
            lista.append(list[1])
            lista.reverse()
            list.remove(list[0])
            list.remove(list[0])
            list.append(lista[0])
            list.append(lista[1])
            list=list[3:] +list[:3]
def listToString(list):
    str1 = " "
    return (str1.join(list))
print(listToString(list))