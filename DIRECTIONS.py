listc = []
while True:
    x = input('')
    if x == 'SCHOOL':
        break
    else:
        if x == 'R':
            x = 'LEFT'
        elif x == 'L':
            x = 'RIGHT'
        listc.append(x)
listc.reverse()
listc.append('HOME')
i = 0
while True:

    if i < len(listc) - 3:
        print('Turn %s onto %s street.' % (listc[i], listc[i + 1]))
        i += 2
    else:
        break
if listc[-2] == 'RIGHT':
    print('Turn RIGHT into your HOME.')
if listc[-2] == 'LEFT':
    print('Turn LEFT into your HOME.')
