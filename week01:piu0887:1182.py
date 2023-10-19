import sys

input = sys.stdin.readline

def back_tracking(s,idx,cnt):
    global count,S

    if s==S and cnt >0:
        count += 1
    for i in range(idx,N):
        back_tracking(s+arr[i],i+1,cnt+1)
    

N,S = map(int,input().split())
arr = list(map(int,input().split()))
count = 0

back_tracking(0,0,0)
print(count)


