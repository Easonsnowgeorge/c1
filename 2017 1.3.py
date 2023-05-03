start = input()
end = input()
charge = int(input())
start = start.split()
end = end.split()
startX = int(start[0])
startY = int(start[1])
endX = int(end[0])
endY = int(end[1])
dx = endX - startX
dy = endY - startY
if startX <= 0:
    dy = endX + startX
    distance = dx + dy
if startY <= 0:
    dy = endY + startY
    distance = dx + dy
distance = dx + dy
if (charge == abs(distance)) or (charge % 2 == 0 and abs(distance) % 2 == 0) or (charge % 2 != 0 and abs(distance) % 2 == 1):
    print ("Y")
else:
    print("N")