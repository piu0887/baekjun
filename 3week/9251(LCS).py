import sys
input = sys.stdin.readline

list_y = list(map(str,input().strip()))
list_x = list(map(str,input().strip()))

dp = [[0]*(len(list_y)+1) for _ in range(len(list_x)+1)]

for j in range(1,len(list_x)+1):
    for i in range(1, len(list_y)+1):
        if list_x[j-1] == list_y[i-1] :
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j-1][i],dp[j][i-1])

print(dp[len(list_x)][len(list_y)])