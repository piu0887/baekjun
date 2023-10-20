# 전위 순회 (루트-왼쪽-오른쪽)은 루트를 방문하고, 왼쪽 서브트리, 
# 오른쪽 서브 트리를 순서대로 방문하면서 노드의 키를 출력한다. 
# 후위 순회 (왼쪽-오른쪽-루트)는 왼쪽 서브트리, 오른쪽 서브트리, 루트 노드 순서대로 키를 출력한다. 
# 예를 들어, 위의 이진 검색 트리의 전위 순회 결과는 50 30 24 5 28 45 98 52 60 이고, 
# 후위 순회 결과는 5 28 24 45 30 60 52 98 50 이다.

# 이진 검색 트리를 전위 순회한 결과가 주어졌을 때, 이 트리를 후위 순회한 결과를 구하는 프로그램을 작성

#입력 : 트리를 전위 순회한 결과가 주어진다. 노드에 들어있는 키의 값은 106보다 작은 양의 정수이다. 
# 모든 값은 한 줄에 하나씩 주어지며, 노드의 수는 10,000개 이하이다. 같은 키를 가지는 노드는 없다.

# 출력: 입력으로 주어진 이진 검색 트리를 후위 순회한 결과를 한 줄에 하나씩 출력

import sys
sys.setrecursionlimit(10**6)

#입력받을 원소 리스트
num_list=[]
while True:
    try:
        num=int(input())
        num_list.append(num) # 리스트로 입력을받는다
    except:
        break

def postorder(left,right): #후위 순회 검색 함수
    #순서 역전시 종료
    if left>right:
        return
    else:
        mid=right+1        #i (0부터 시작하여) 오른쪽과 비교 -> 크다면 분할하여 후위 순회
        for i in range(left+1,right+1):
            #해당 원소가 현재 노드보다 크다면 그 전까지는 왼쪽 서브 트리,
            #해당 원소 이후는 오른쪽 서브 트리이다.
            if num_list[left]<num_list[i]: #오른쪽 원소가 크면 자른다.
                mid=i
                break
        postorder(left+1,mid-1)
        postorder(mid,right)
        print(num_list[left])

postorder(0,len(num_list)-1)