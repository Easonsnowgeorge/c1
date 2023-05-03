a = int(input())
b = int(input())
sumac = [a, b]
c = 1
while sumac[c-1] >= sumac[c]:
    sumac.append(sumac[c-1] - sumac[c])
    c+=1
print(len(sumac))
print(sumac)