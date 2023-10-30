import sys

input = sys.stdin.readline

info = input().split('-')

ans = 0

for i in info[0].split('+'):
    ans += int(i)
for i in info[1:]:
    for j in i.split('+'):
        ans -= int(j)

print (ans)
