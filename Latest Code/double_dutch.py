def double_dutch():
    global sudoku_board
    string=''
    vital_pts=[[2,3],[2,2],[1,3],[0,4],[1,5],[2,6],[2,5],[3,6],[4,7],[4,6],[4,5],[5,6],[6,7],[6,6],[6,5],[7,4],[6,3],[6,2],[6,1],[5,2],[4,3],[4,2],[4,1],[3,2]]
    for i in range(0,len(vital_pts)):
        string+=str(sudoku_board[vital_pts[0],vital_pts[1]])
    if string!=string[::-1]:
        return False
    else:
        if sudoku_board[0,2]>sudoku_board[1,2] or sudoku_board[1,2]>sudoku_board[2,2]:
            return False
        elif sudoku_board[0,3]>sudoku_board[1,3] or sudoku_board[1,3]>sudoku_board[2,3]:
            return False
        elif sudoku_board[0,4]<sudoku_board[1,4] or sudoku_board[1,4]<sudoku_board[2,4]:
            return False
        elif sudoku_board[0,5]<sudoku_board[1,5] or sudoku_board[1,5]<sudoku_board[2,5]:
            return False
        elif sudoku_board[0,6]<sudoku_board[1,6] or sudoku_board[1,6]<sudoku_board[2,6]:
            return False
        elif sudoku_board[8,2]<sudoku_board[7,2] or sudoku_board[7,2]<sudoku_board[6,2]:
            return False
        elif sudoku_board[8,3]<sudoku_board[7,3] or sudoku_board[7,3]<sudoku_board[6,3]:
            return False
        elif sudoku_board[6,5]<sudoku_board[7,5] or sudoku_board[6,5]<sudoku_board[8,5]:
            return False
        elif sudoku_board[8,6]<sudoku_board[7,6] or sudoku_board[7,6]<sudoku_board[6,6]:
            return False
        elif sudoku_board[0,8]<sudoku_board[0,7] or sudoku_board[0,7]<sudoku_board[0,6]:
            return False
        elif sudoku_board[1,0]<sudoku_board[1,1] or sudoku_board[1,1]<sudoku_board[1,2]:
            return False
        elif sudoku_board[2,0]<sudoku_board[2,1] or sudoku_board[2,1]<sudoku_board[2,2]:
            return False
        elif sudoku_board[2,6]<sudoku_board[2,7] or sudoku_board[2,7]<sudoku_board[2,8]:
            return False
        elif sudoku_board[2,0]<sudoku_board[2,1] or sudoku_board[2,1]<sudoku_board[2,2]:
            return False
        elif sudoku_board[2,6]<sudoku_board[2,7] or sudoku_board[2,7]<sudoku_board[2,8]:
            return False
        elif sudoku_board[5,8]<sudoku_board[5,7] or sudoku_board[5,7]<sudoku_board[5,6]:
            return False
        elif sudoku_board[6,6]<sudoku_board[6,7] or sudoku_board[6,7]<sudoku_board[6,8]:
            return False
        elif sudoku_board[6,2]<sudoku_board[6,1] or sudoku_board[6,1]<sudoku_board[6,0]:
            return False
        elif sudoku_board[7,2]<sudoku_board[7,1] or sudoku_board[7,1]<sudoku_board[7,0]:
            return False
        elif sudoku_board[8,2]<sudoku_board[8,1] or sudoku_board[8,1]<sudoku_board[8,0]:
            return False
    return True
