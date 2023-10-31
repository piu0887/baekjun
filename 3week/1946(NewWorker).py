import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):

    N = int(input())
    volun = []
    

    for _ in range(N):
        score_doc, score_inter = map(int, input().split())
        volun.append((score_doc,score_inter))


    volun.sort(key= lambda x : x[1])
    min = volun[0][0]
    count = 1

    for i in range(1,N):
        if volun[i][0] < min:
            min = volun[i][0]
            count +=1
    print(count)

