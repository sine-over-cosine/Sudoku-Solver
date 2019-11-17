def quadrant_check(board,row,col,val):
    if row>=0 and row<3:
        if col>=0 and col<3:
            return quad1_check(board,val)
        elif col>=3 and col<6:
            return quad2_check(board,val)
        else:
            return quad3_check(board,val)
    elif row>=3 and row<6:
        if col>=0 and col<3:
            return quad4_check(board,val)
        elif col>=3 and col<6:
            return quad5_check(board,val)
        else:
            return quad6_check(board,val)
    elif row<=6 and row<9:
        if col>=0 and col<3:
            return quad7_check(board,val)
        elif col>=3 and col<6:
            return quad8_check(board,val)
        else:
            return quad9_check(board,val)
        
def quad1_check(board,val):
    return val in board[0:3,0:3]
    
def quad2_check(board,val):
    return val in board[0:3,3:6]
    
def quad3_check(board,val):
    return val in board[0:3,6:9]

def quad4_check(board,val):
    return val in board[3:6,0:3]

def quad5_check(board,val):
    return val in board[3:6,3:6]
    
def quad6_check(board,val):
    return val in board[3:6,6:9]
    
def quad7_check(board,val):
    return val in board[6:9,0:3]
    
def quad8_check(board,val):
    return val in board[6:9,3:6]
    
def quad9_check(board,val):
    return val in board[6:9,6:9]
