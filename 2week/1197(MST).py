# 문제: 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다

# 입력: 첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 
# 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 
# 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며,
# 절댓값이 1,000,000을 넘지 않는다.

# 그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 
# 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 
# 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

# 출력: 첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.

import sys
input=sys.stdin.readline

v, e = map(int, input().split())

#부모 테이블 초기화
parent = [0] * (v+1)
for i in range(1, v+1) :
    parent [i] = i

# find 연상
def find_parent(parent,x) :
    if parent[x] != x:
        parent [x] = find_parent(parent,parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
edges = []
total_cost = 0

# 간선 정보 주어지고 비용을 기준으로 정렬
for _ in range(e):
    a, b, cost = map(int, input().split()) 
    edges.append((cost, a, b))

# 간선 정보 비용 기준으로 오름차순 정렬
edges.sort()

# 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
for i in range(e) :
    cost, a, b = edges[i] 
    # find 연산 후, 부모노드 다르면 사이클 발생 x이므로 union 연산 수행 -> 최소 신장 트리에 포함
    if find_parent(parent, a) != find_parent(parent,b) :
        union_parent(parent, a , b)
        total_cost += cost

print(total_cost)