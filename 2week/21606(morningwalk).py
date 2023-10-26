import sys
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
A = list(map(int,list(input().strip()))) # ****
check = [1]                              # **** 알아보기
for i in A:
     check.append(i)


for _ in range(N-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


count = 0

def dfs(start):
    global count,visited
    visited[start] = True
    for v in graph[start]:
        if check[v] == 1 and not visited[v] :
            visited[v] = True
            count +=1
        elif check[v] ==0 and not visited[v] :
            visited[v] = True
            dfs(v)  
    
    
for i in range(1,N+1):
    visited = [False] * (N+1)
    if check[i] == 1:
         dfs(i)


print(count)
