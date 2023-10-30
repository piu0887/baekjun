import sys

input = sys.stdin.readline

N, K = map(int, input().split())

A_list= [] 

for _ in range(N):
    A_list.append(int(input()))

count = 0

for i in range(N):
    if A_list[N-i-1] > K :
        continue
    elif A_list[N-i-1] <= K :
        count = K//A_list[N-i-1] + count
        K = K%A_list[N-i-1]
        if K == 0 :
            print(count)
            break
    

