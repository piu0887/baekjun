import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
K = int(input())
A = [[*map(int,input().split())] for _ in range(K)]
L = int(input())
M = [*map(lambda x: (int(x[0]),x[1]),[input().split() for _ in range(L)])]
MAXTIME = 10001
B = [[0]*N for _ in range(N)] # 보드
directions = [(-1,0),(0,1),(1,0),(0,-1)] #시계방향  상, 우, 하, 좌
directIndex = 1
ahead = directions[directIndex] # 현재 방향
commands = deque()
for m in M:
    commands.append(m)
for apple in A:   ## 사과 셋팅
    B[apple[0]-1][apple[1]-1]=1 # 바닥 0, 사과 1, 뱀 2
snake = deque()
snake.append((0,0))
def mapSnake(board ,snake):
    for body in snake:
        board[body[0]][body[1]]=2
def printBoard(B,X):
    print(X,"초")
    for line in B:
        print(' '.join([*map(str,line)]))
for X in range(1,MAXTIME):
    nexthead = (snake[-1][0]+ahead[0],snake[-1][1]+ahead[1])
    coordX = nexthead[0]
    coordY = nexthead[1]
    if(0<=coordX<N and 0<=coordY<N and B[coordX][coordY]!=2):
        snake.append(nexthead)
        # print("늘림",snake)
        if(B[coordX][coordY]!=1):
            v=snake.popleft()
            B[v[0]][v[1]]=0
            # print("줄임",snake)
    else:
        print(X)
        break
    if commands and X==commands[0][0]:
        c=commands.popleft()
        if c[1]=="D":
            directIndex +=1
            # print("시계방향")
        if c[1]=="L":
            directIndex -=1
            # print("반시계방향")
        directIndex %=4
        ahead = directions[directIndex]
    mapSnake(B,snake)
    # printBoard(B,X)
