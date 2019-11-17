def col_check(board,col,val):
    for i in range(0,9):
        if board[i,col]== val:
            return False
    return True
    
def row_check(board,row,val):
    for i in range(0,9):
        if board[row,i]== val:
            return False
    return True
