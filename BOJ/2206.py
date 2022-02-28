from collections import deque

n,m = map(int, input().split())
graph = [list(map(int,input()) for _ in range(n))]
vis = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0 -1]

def bfs(x,y,cr,vis,graph):
    queue = deque()
    queue.append()