import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

dp[0] = 1

dp[1] = 2

for i in range(2,N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

answer = (dp[N-1])

print(answer)