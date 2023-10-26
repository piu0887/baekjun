import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
graph=[[] for i in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

for _ in range(1,N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            answer[i] = start
            dfs(graph,i)

dfs(graph,1)

for x in range(2, N+1):
    print(answer[x])