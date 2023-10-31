import sys
input = sys.stdin.readline

N = int(input())

time_table = []

for _ in range(N):
    time_start, time_end = map(int, input().split())
    time_table.append((time_start, time_end))

time_table.sort(key= lambda x : (x[1], x[0]))

count = 1
last_con = time_table[0][1]

for i in range(1,N):
    if time_table[i][0] >= last_con:
        last_con = time_table[i][1]
        count +=1

print(count)