# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
import sys
input = sys.stdin.readline

n = int(input())
if n > 15 or n < 1 :
    pass
else :

    answer = 0
    rows = [0] * n

    # 현재 놓은 퀸 자리가 유효한지 체크
    def is_check(r):
        for i in range(r):
            # 세로 체크 or 대각선 체크
            if rows[i] == rows[r] or abs(r - i) == abs(rows[r] - rows[i]):
                return False
        return True

    # r행에 퀸을 놓아보기
    def put_queen(r):
        global answer
        if r == n:
            answer += 1
            return
        
        for i in range(n):
            rows[r] = i
            if is_check(r):
                # 해당 자리에 놓을 수 있다면 다음행으로!
                put_queen(r + 1)
                
    put_queen(0)
    print(answer)

    
