lines = int(input())
for i in range(lines) :
    text = list(input())
    j = 0
    printStuff = [[text[0], 1]]
    counter = 0
    while j < len(text) - 1 :
        if text[j] == text[j + 1] :
            printStuff[counter][1] += 1
        else :
            printStuff.append([text[j + 1], 1])
            counter += 1
        j += 1
    for x in range(len(printStuff)) :
        print(printStuff[x][1], end = " ")
        print(printStuff[x][0], end=" ")
    print()