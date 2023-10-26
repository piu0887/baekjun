N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(input()))
visit = [[False]*M for i in range(N)]
 
def dfs_horizon(x,y):
    if x<0 or y<0 or x>=M or y>=N :
        return 0
    if visit[y][x] == False and arr[y][x]== '-':
        visit[y][x] = True
        arr[y][x] = 0
        return dfs_horizon(x+1,y)
    return 0
 
def dfs_vertical(x,y):
    if x<0 or y<0 or x>=M or y>=N :
        return 0 
    if visit[y][x] == False and arr[y][x]== '|':
        visit[y][x] = True
        arr[y][x] = 0
        return dfs_vertical(x,y+1)
    return 0
 
count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '-':
            count += 1
            dfs_horizon(j,i)
        elif arr[i][j] == '|':
            count += 1
            dfs_vertical(j,i)
print(count)