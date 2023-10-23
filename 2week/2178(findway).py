from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):                                # 행반복하여 열은 append.list로 입력받은
     graph.append(list(map(int,input()))) # 띄워쓰기 없이 입력받을 경우




def bfs (x, y):
    #미로 문제 풀 때는 이동을 표현해준다.
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append((x, y)) # queue 먼저 생성 후 튜플로 선언
    
    while queue:
        x, y = queue.popleft()
        # 현재위치에서 4가지 방향
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # if 0 <= next_x < n and 0<= next_y < m :
            #     break
            if next_x < 0 or next_x >= n or next_y <0 or next_y>= m :
                continue

            if graph[next_x][next_y] == 0:
                continue

        
            if graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1
                # graph[next_x][next_y] = graph[x][y] + 1 #value 자체를 이동횟수로 사용

    return graph[n-1][m-1]

print (bfs(0,0))