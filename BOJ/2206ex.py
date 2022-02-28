import sys
from collections import deque

def bfs():
    q.append([0, 0, 0])
    vis[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]
            if 0 <= dx < n and 0 <= dy < m:
                if graph[dx][dy] == 0 and vis[dx][dy][z] == -1:
                    vis[dx][dy][z] = vis[x][y][z] + 1
                    q.append([dx, dy, z])
                elif graph[dx][dy] == 1 and vis[dx][dy][1] == - 1 and z ==0:
                    vis[dx][dy][1] = vis[x][y][z] + 1
                    q.append([dx, dy, 1])

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))
vis = [[[-1] * 2 for _ in range(m)] for _ in range(n)]
q = deque()
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
bfs()
case1, case2 = vis[n - 1][m - 1][0], vis[n - 1][m - 1][1]
if case1 == -1 and case2 != -1:
    print(case2)
elif case1 != -1 and case2 == -1:
    print(case1)
else:
    print(min(case1, case2))