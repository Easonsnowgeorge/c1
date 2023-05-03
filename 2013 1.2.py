a = input()
b = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
for i in range(len(a)):
    if a[i] not in b:
        print("NO")
        break
    if i == len(a) - 1:
        print("YES")