from collections import deque
import sys

input = sys.stdin.readline

def bfs (x,y):
    global count
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    graph[x][y] = 0
    queue = deque()
    queue.append((x,y))
    while queue:
        now = queue.popleft()
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if 0 <= next_x < N and 0<= next_y < N and graph[next_x][next_y] ==1 :
                graph[next_x][next_y] = 0
                count +=1
                queue.append((next_x,next_y))

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int,input().strip())))

answer = []

for x in range(N):
    for y in range(N):
        if graph[x][y] ==1:
            count = 1
            bfs(x,y)
            answer.append(count)

sorted(answer)
print(len(answer))
for k in range(len(answer)):
    print(answer[k])

    
