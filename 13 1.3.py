x, y = list(map(int, input().split()))
curx = 0
cury = 0
while True:
    a, b = list(map(int, input().split()))
    if a == 0 and b == 0:
        break
    if curx + a <= x and curx + a >= 0:
        curx += a
    if curx + a < 0:
        curx = 0
    elif curx + a > x:
        curx = x


    if (cury + b) <= y and (cury + b) >= 0:
        cury += b
    elif (cury + b) < 0:
        cury = 0
    else:
        cury = y
    print(curx, cury)