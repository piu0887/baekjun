import sys
input = sys.stdin.readline

T = int(input())
ans =[]

for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split())) # coin 배열 리스트를 만들고
    coin.insert(0,0) # 2차원 배열을 만든다.
    M = int(input())
    dp = [[0]*(M+1) for _ in range(N+1)]
   
    for i in range(N+1):
        dp[i][0] = 1

    for j in range(1,N+1):
        for i in range(1,M+1):
            dp[j][i] = dp[j-1][i]
            if i - coin[j] >= 0:
                dp[j][i] += dp[j][i-coin[j]]

    ans.append(dp[N][M])

for i in range(len(ans)):
    print(ans[i])