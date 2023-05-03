
l = []
l1 = []
for i in range(len(s)):
    total = 1
    for j in range(i, len(s)-1):
        if s[j]>s[j+1]:
            break
        if s[j]<= s[j+1]:
            total += 1
    l1.append(total)
max = max(l1)
place = l1.index(max)
print("Longest substring in alphabetical order is: %s" %(s[place:place+max]))