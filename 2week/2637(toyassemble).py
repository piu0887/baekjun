import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
needs = [0] * (N+1) # 각 부품의 필요 테이블 (진입차수)
ans = [0] * (N+1)
ans[N] = 1

for _ in range(M) :
    a,b,c = map(int, input().split()) # a= 만드려는 부품 b = 필요한 부품 c= 필요 부품갯수
    graph[a].append((b,c))              # a에 b부품이 c만큼 필요한 정보입력
    needs[b] += 1                   # b 부품 진입차수 1 증가

queue = deque([N])
table = [i for i in range(1, N+1) if not graph[i]] # **********

#위상 정렬시작
while queue:
    now = queue.popleft()
    #현 제품의 다음 단계 번호, 현제품이 얼마나 필요한지
    for next, count in graph[now]:
        needs[next] -=1
        ans[next] += count * ans[now]
        if not needs[next]:
            queue.append(next)

for i in table:
    print(i,ans[i])