import copy
N=int(input())
def set(n,row,board):
    ans = 0
    for col in range(n):
        cond=True
        for ro,co in enumerate(board):
            if(col==co or co-ro==col-row or ro+co==row+col): # 대각선 비교
                cond = False
                break
        if not cond: continue
        board[row]=col
        if row==n-1 : return 1
        ans += set(n,row+1,copy.copy(board))
    return ans
board = [-100]*N # None 으로 할 시 비교 불가라 오류 발생
result = set(N,0,board)
print(result)