import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph=[]
for _ in range(N):
    graph.append(list(input()))

visited = [[False] * (M) for _ in range(N)]


def dfs_horizon(y,x):
    if x<0 or y<0 or x>=M or y>=N :
        return 0
    if visited[y][x] == False and graph[y][x] == '-':
        visited[y][x] = True
        graph[y][x] = 0 
        return dfs_horizon(y,x+1)
    return 0

def dfs_vertical(y,x) :
    if x<0 or y<0 or x>=M or y>=N :
        return 0
    if visited[y][x] == False and graph[y][x] =='|':
        visited[y][x] = True
        graph[y][x] = 0
        return dfs_vertical(y+1,x)
    return 0

count = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] =='-' :
            count+=1
            dfs_horizon(i,j)
        elif graph[i][j] =='|':
            count+=1
            dfs_vertical(i,j)

print(count)

