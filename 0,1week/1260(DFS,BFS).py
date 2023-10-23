# 문제 : 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다

# 입력: 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다

# 출력: 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
# V부터 방문된 점을 순서대로 출력하면 된다.

import sys
input = sys.stdin.readline

N,M,V = map(int, input().split())

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a, b = map(int, input().split())
    graph [a][b] = graph [b][a] = 1 #정점 끼리 양방향을 표시

#방문 리스트 행렬
visited1 = [0]*(N+1)
visited2 = visited1.copy()

#DFS함수 만들기
def dfs(V):
    visited1[V] = 1 # 스택에 담겼는지 방문처리
    print(V, end=' ')
    for i in range(1,N+1):
        if graph[V][i] == 1 and visited1[i] == 0:  #graph V-i가 연결되었나 and graph[i]는 스택에 들어간적이 있나
            dfs(i)

#BFS함수 만들기
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) # 방문노드제거
        print(V,end=' ')
        for i in range(1, N+1) :
            if(visited2[i]==0 and graph[V][i] == 1):
                queue.append(i)
                visited2[i] = 1 # 방문처리

#                 bfs는 queue를 이용한다.
# 탐색 시작 노드 V가 주어진다면
# queue = [V] 로 큐에 탐색 노드를 먼저 넣는다.
# 이 후, 위에서 만들어놓은 방문리스트 visited2[V] = 1로 방문 처리해준다.
# V가 1이라면 visited2 = [0,1,0,0]이 될 것이다.
# dfs와 같은 원리이다.

# 이제 while queue: 로 queue에 값이 없을때까지(탐색이 끝날때까지) 반복할 것이다.
# 먼저 queue.pop(0)을 해준다. 이 코드는 queue에서 0번째 요소를 돌려주고 삭제하라는 것이다.
# queue는 선입선출 구조이므로 가장 먼저들어온 0번째 요소부터 빼는 것이다.
# 그리고 삭제한 요소를 V변수로 돌려받겠다.
# 위에서 V를 1로 가정했을 때 queue = [1], visited[2] = [0,1,0,0]인 상태이고
# 여기서 V = queue.pop(0)을 해주면 queue = []이 되고, V = 1이 될 것이다.
# 1을 뺐으니 1을 출력한다. print(V, end = ' ')

# 이 후 for문으로 연결된 노드들을 탐색해줄 것이다.
# 원리는 위에 설명한 dfs와 같다.
# V와 연결되고, 방문한 적이 없는 노드가 있다면
# 큐에 넣어줄 것이다.


# bfs과정을 나열해보겠다.
# V = 1 // 1번 노드부터 탐색시작
# queue = [1] // 방문 노드 저장
# visited2[1] = 1 // visited2 = [0,1,0,0]

# while문 들어가서,
# queue = []
# V = 1 // 1출력
# for문 들어가서,
# 노드 1과 2가 연결되고, 노드 2가 방문된적이 없다면
# graph[1][2] ==1 and visited2[2] == 0에 해당하므로
# queue = [2]
# visited2[2] = 1로 방문처리

# 노드 1과 3이 연결되고, 노드 3이 방문된적이 없다면
# queue = [2,3]
# visited2[3] = 1로 방문처리
# 모든 연결 노드 확인 후 for문 반복 끝

# queue에 값이 있으므로
# while문 탈출 안하고 다시 반복
# V = 2 // 2출력
# queue = [3]
# graph[2][1] == 1 and visited2[2] ==0에 해당하지 않으므로 큐에 다시 넣지 못한다.(2는 1과 연결돼있지만, 1은 이미 큐에 들어간 기록이 있다.)
# graph[2][3] == 1 and visited2[2] ==0 역시 마찬가지로 방문기록이 있으므로 false

# 이 경우 아무것도 추가되지 않고 for문을 빠져나간다.
# queue = [3]으로 아직 값이 있으므로 while문 다시 반복
# V = 3 
# queue = []

dfs(V)
print()
bfs(V)