#N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 
# 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다

import sys
input=sys.stdin.readline

size=int(input())
info=list(map(int, input().split()))
search=int(input())
find=list(map(int, input().split()))
info=sorted(list(info))

def binary_search(n, info, start, finish):
    if start>finish:
        return 0
    mid=(finish+start)//2
    if info[mid]==n:
        return 1
    elif info[mid]>n:
        return binary_search(n,info,start,mid-1)
    else:
        return binary_search(n,info,mid+1,finish)

for num in find:
    print(binary_search(num, info,0,size-1))
    