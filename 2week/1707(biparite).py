import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

K = int(input())

def dfs(node) :
    global result

    for neighbor in graph[node]:
        # 이웃노드에 색일 칠해져 있지 않다면
        if (visited[neighbor] == -1):

            if(visited[node] == 1):
                visited[neighbor] = 2
            if(visited [node] == 2):
                visited[neighbor] = 1

            dfs(neighbor)
        # 이웃노드에 색이 칠해져 있다면
        else: 
            # 현재 노드와 동일한 색이라면

            if (visited[node] == visited[neighbor]):
                result = False
                return


for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [-1] * (V + 1)
    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    #이분 그래프 여부
    result = True

    for i in range (1, V +1):
        if (visited[i] == -1):
            visited[i] = 1
            dfs(i)
            if (result == False):
                break

    if (result == False):
        print('NO')
       
    else : 
        print('YES')
    