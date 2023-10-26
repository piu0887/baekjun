import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

add,sub,mul,div = map(int,input().split())

#최댓값 최솟값 초기화 !!!!!정수로 선언할것!!!!
max_value = int(-1e9)
min_value = int(1e9)

def dfs(i,arr):
    global add, sub, mul, div, max_value, min_value

    
    #주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
    if i == N :
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)


    else:
        #더하기
        if add > 0:
            add -= 1
            dfs(i+1,arr + data[i])
            add +=1
        if sub> 0:
            sub -=1
            dfs(i+1, arr - data[i])
            sub += 1
        if mul > 0 :
            mul -=1
            dfs(i+1,arr * data[i])
            mul +=1
        if div> 0 :
            div -= 1
            if arr < 0:
                dfs(i+1, int(arr/data[i]))
                div +=1
            else:
                dfs(i+1,int(arr/data[i]))
                div +=1

#dfs 매서드 호출
dfs(1,data[0])

print(max_value)
print(min_value)


