n = int(input())
a=[]

for _ in range(n):
    num = int(input())
    a.append(num)


for i in range(len(a)-1, 0 , -1):
    for j in range(i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    

for k in range(len(a)):
    print(a[k])