import sys
import collections
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == n-1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print('-1')
        else:
            print(dist[i])