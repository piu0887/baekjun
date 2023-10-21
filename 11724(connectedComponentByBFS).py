# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
#   (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
from collections import deque

input = sys.stdin.readline

def bfs (start) :
    queue = deque([start])
    visited[start] = True # 방문처리
    while queue :
        node = queue.popleft()      # 노드를 큐에서 꺼낸 후
        for i in graph[node]:
            if not visited[i] :     #방문기록 없으면 방문처리 후 queue에 인큐
                visited[i] = True
                queue.append(i)

N,M = map(int, input().split())
graph =[[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u) # u v 양 방향성


visited = [False] * (N+1)
count = 0                 # component 갯수 저장


for i in range (1, N + 1):           # N개의 노드를 각 돌면서
    if not visited[i] :              # 방문기록확인
        if not graph[i] :            # 방문안했고 그래프가 비어있으면 count +1 
            count += 1
            visited[i] = True        # 방문처리
        else:                        # 방문을 안했는데 그래프가 비어있지 않으면
            bfs(i)                   # Bfs i를 시작점으로 돈다
            count += 1                # 그리고 count + 1 

print(count)