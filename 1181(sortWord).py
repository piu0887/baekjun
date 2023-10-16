Num=int(input())
Word=[input().strip() for _ in range(Num)]
Sor=sorted(sorted(set(Word)),key=len)
print('\n'.join(Sor))