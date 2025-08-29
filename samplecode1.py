import numpy as np
a=np.zeros((9,9),dtype=int)
a[0][3]=5
a[4][2]=7
print(a)
def row_check(board,row,col,num):
    board[row]
    if num in board[row]:
        return False
    return True
def col_check(board,row,col,num):
    board[:,col]
    if num in board[:,col]:
        return False
    return True
def box_check(board,row,col,num):
    start_row=row-(row%3)
    start_col=col-(col%3)
    for i in range(3):
        for j in range(3):
            cell=board[start_row+i][start_col+j]
            if(cell==num):
                return False
            else:
                return True
def is_safe(board,row,col,num):
    return(row_check(board,row,col,num), col_check(board,row,col,num),box_check(board,row,col,num))





