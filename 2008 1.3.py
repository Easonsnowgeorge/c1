def gps():
    word = input()
    word = 'A'+word+'e'
    array = ['ABCDEF','GHIJKL','MNOPQR','STUVWX','YZ -.e']
    list = []
    for i in range(len(word)):
        let = word[i]
        for a in range(len(array)):
            if let in array[a]:
                x = a+1
                y = array[a].index(word[i])+1
                list.append((x,y))
    moves = 0
    for c in range(len(list)-1):
        moves+=abs(list[c+1][0]-list[c][0])
        moves+=abs(list[c+1][1]-list[c][1])
    print(moves)
gps()