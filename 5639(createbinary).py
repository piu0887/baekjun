import sys
sys.setrecursionlimit(10**6)

binary_tree={}        #이진 트리를 위한 딕셔너리 선언
while True:
    try:
        num=int(input())
        if len(binary_tree)==0:        #빈 트리일 때
            root=num                   #루트로 설정
            binary_tree[root]=['*','*']#루트 왼쪽 오른쪽 빈값 생성
        else:
            curr=root
            while True:
                #왼쪽 서브 트리일 때
                if num<curr:
                    #왼쪽 노드가 없을 때
                    if binary_tree[curr][0]=='*': #왼쪽 비어있을떄
                        binary_tree[curr][0]=num #왼쪽 서브트리에 키값 입력 후
                        binary_tree[num]=['*','*'] #서브트리 빈값 생성
                        break
                    #왼쪽 자식 노드로 이동
                    else:
                        curr=binary_tree[curr][0]
                #오른쪽 서브 트리일 때
                else:
                    #오른쪽 노드가 없을 때
                    if binary_tree[curr][1]=='*':
                        binary_tree[curr][1]=num
                        binary_tree[num]=['*','*']
                        break
                    #오른쪽 자식 노드로 이동
                    else:
                        curr=binary_tree[curr][1]
    except:
        break

def postorder(curr):
    #왼쪽 자식 노드로 이동
    if binary_tree[curr][0]!='*':
        postorder(binary_tree[curr][0])
    #오른쪽 자식 노드로 이동
    if binary_tree[curr][1]!='*':
        postorder(binary_tree[curr][1])
    #현재 노드 출력
    print(curr)

postorder(root)