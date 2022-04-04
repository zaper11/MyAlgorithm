n, m, x, y, k = map(int,input().split())

bd = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
die = [0, 0, 0, 0, 0, 0]
for i in range(n):
    bd.append(list(map(int, input().split())))
com = list(map(int,input().split()))

def go(dir):
    a, b, c, d, e, f = die[0], die[1], die[2], die[3], die[4], die[5]
    if dir == 1:
        die[0], die[1], die[2], die[3], die[4], die[5] = d, b, a, f, e, c

    elif dir == 2:
        die[0], die[1], die[2], die[3], die[4], die[5] = c, b, f, a, e, d

    elif dir == 3:
        die[0], die[1], die[2], die[3], die[4], die[5] = e, a, c, d, f, b

    else:
        die[0], die[1], die[2], die[3], die[4], die[5] = b, f, c, d, a, e

nx, ny = x, y
for i in com:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    go(i)
    if bd[nx][ny] == 0:
        bd[nx][ny] = die[-1]
    else:
        die[-1] = bd[nx][ny]
        bd[nx][ny] = 0
    print(die[0])