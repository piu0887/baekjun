import heapq
import sys
input = sys.stdin.readline

def check_range(x,y) :
    return (0 <= x < N) and (0 <= y < N)

def dijkstra(x,y):
    queue = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited = [[0 for _ in range(N)] for _ in range(N)] # N x N 바둑판 방문 배열 생성

    heapq.heappush(queue, (0, x, y)) # 큐에 시작점 정보 삽입
    visited[x][y] = True # 시작점 방문처리
    while queue:
        cost, now_x, now_y = heapq.heappop(queue) #큐에서 비용과 x,y 방향 꺼냄
        if now_x == N-1 and now_y == N-1: # 끝지점에 도달했을 경우
            return cost
        for i in range(4): # 다음 방향 선택 4가지 선택
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            # 이동 지점이 바둑판 안쪽인지 방문여부 확인
            if check_range(next_x, next_y) and visited[next_x][next_y] == 0: 
                    visited[next_x][next_y] = True # 이동지점 방문처리
                    #   만약 이동 지점이 흰색이라면, cost 발생없음
                    if graph[next_x][next_y]:
                         heapq.heappush(queue, (cost, next_x, next_y))
                    # 만약 이동 지점이 검은색이라면, cost +1 
                    else:
                         heapq.heappush(queue,(cost + 1, next_x, next_y))

N = int(input())
graph = []
# 바둑판 정보 입력
for _ in range(N):
     graph.append(list(map(int, input().strip())))
# 비용 결과값 저장
result = dijkstra(0, 0)
print(result)