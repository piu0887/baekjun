import sys
input = sys.stdin.readline

N, K = map(int, input().split())

W_V=[]

for _ in range(N):
    weight,value = map(int, input().split())
    W_V.append((weight, value))

happy_junseo = [[0]*(K+1) for _ in range(N+1)]

# 조건 
# 1) 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전 물건][같은 무게] (happy_junseo[j-1][i]를 입력해준다.

# 2) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(happy_junseo[j-1][i-W_V[j-1][0]]을 위의 행에서 가져와 더해준다.

# 3) 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는 값(happy_junseo[j-1][i])을 가져온다.

for j in range(1,N+1):
    for i in range(1,K+1):
        if i < W_V[j-1][0]:
            happy_junseo[j][i] = happy_junseo[j-1][i]
        else:
         happy_junseo[j][i] = max((W_V[j-1][1] + happy_junseo[j-1][i-W_V[j-1][0]]),happy_junseo[j-1][i])

print (happy_junseo[N][K])