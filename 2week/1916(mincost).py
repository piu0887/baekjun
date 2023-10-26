import sys
import heapq

input = sys.stdin.readline

N= int(input())
M= int(input())



graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))       #도착지 가중치 정보 삽입

start, end = map(int, input().split())

def dijkstra(graph,start):
    queue = []
    INF = int(1e9) 
    distances = [INF] * (N+1)    # 처음값 초기화
    distances[start] = 0         #시작 노드까지의 거리 0
    heapq.heappush(queue,[distances[start],start])   # 시작노드부터 탐색
    
    while queue:                         # queue에 노드가 없을때 까지
        dist,node = heapq.heappop(queue) # 탐색할 노드, 거리
        # 기존 최단거리보다 멀다면 무시
        if distances[node] < dist :
            continue
        # 노드와 연결된 인접노드 탐색
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist # 인접노드까지의 거리
            if distance < distances[next_node]: # 기존 거리보다 짧으면 갱신
                distances[next_node] = distance
                # 다음 인접 거리를 계산하기위에 queue에 삽입
                heapq.heappush(queue,[distance, next_node])
    return distances
            
dist_start = dijkstra(graph,start)
print(dist_start[end])
