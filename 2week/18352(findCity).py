import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().split())

distance = [INF] * (n+1)

visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b = map(int,input().split())
    graph[a].append((b,1))

    
def dijkstra(start) :
    que = []
    heapq.heappush(que,(0,start))
    distance[start] = 0
    visited[start] = True
    while que:
        dist, node = heapq.heappop(que)
        if distance[node] < dist:
            continue
        for next in graph [node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]] :
                distance[next[0]] = cost
                heapq.heappush(que,(cost,next[0]))
    
dijkstra(x)
answer = []
for i in range(1,n+1):
    if distance[i] == k :
        answer.append(i)

if len(answer) == 0:
    print(-1)
else :
    for i in answer :
        print(i) 
