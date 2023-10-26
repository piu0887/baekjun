# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

que=deque()

for i in range(n):
    command = input().split()

    if command[0]=='push':
         que.append(command[-1])
    elif command[0]=='pop':
        if not que:
           print(-1)
        else:
            print(que.popleft())
    elif command[0]=='size':
        print(len(que))
    elif command[0]=='empty':
        if not que:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if not que:
            print(-1)
        else:
            print(que[0])
    elif command[0]=='back':
        if not que:
            print(-1)
        else:
            print(que[-1])



# class MyQue:
#     size = 1000
#     queue = int[size]
#     index = 0
    

#     function push(data):
#         if(index >= size):
#             return false
#         queue[++index] = data
#         return true
#     function pop():
#         if(index <= 0)
#             return -1
#         else :


#         popData = queue[index]
#         index---
#         return popData
