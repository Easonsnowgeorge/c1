def bfs():
    d[0][0] = 0
    t[0][0] = 1
    queue = [(0, 0)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y, = queue.pop(0)
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0<=a < n and 0<= b < m and g[a][b] == "*":
                if d[a][b] != -1 :
                    t[a][b] += t[x][y]
                if d[a][b] == -1:
                    queue.append((a,b))
                    d[a][b] = d[x][y] + 1
                    t[a][b] = t[x][y]
    print(t[n-1][n-1])
    print(d[n-1][n-1]+1)

n,m = map(int,input().split())
g = [list(map(str, input().split())) for i in range(n)]


d = [[-1 for j in range(m)] for i in range(n)]
t = [[0 for j in range(m)] for i in range(n)]
bfs()