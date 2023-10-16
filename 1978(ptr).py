import sys
import math

N = int(input())
ptr = list(map(int,input().split()))

count = 0

for i in ptr:
    if i > 1 :
        for j in range(2,i):
            if i%j==0 :
             break
        else :
             count += 1




print(count)