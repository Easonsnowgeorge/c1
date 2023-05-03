
count=0
for a in range(1,10):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    if a>=b>=c>=d>=e:
                        count+=1

print(count)
print("ok")