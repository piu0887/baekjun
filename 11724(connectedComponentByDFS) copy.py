# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
# (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
#   (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    u, v = map(int, input().split())      #u, v를 입력 받고 graph[u] graph[v]의 양방향성
    graph[u].append(v)                
    graph[v].append(u)

visited = [False] * (N+1)
count = 0

def dfs(start, depth):

    visited[start] = True

    for i in graph[start] :
        if not visited[i]:
            dfs(i, depth + 1)

for i in range(1, N+1):
    if not visited [i]:
        if not graph[i]:
            count +=1
            visited[i] = True
        else :
            dfs(i,0)
            count += 1

print (count)
