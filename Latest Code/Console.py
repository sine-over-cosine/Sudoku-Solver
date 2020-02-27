# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:57:55 2020

@author: RussellTan
"""

#This module implements a Bactracking Approach to solve any sudoku puzzle.
#This is return multiple solutions should there be any
#You can also implement your restrictions from other forms of soduku puzzles from
#Cracking the Cryptic
import numpy as np
import time
def initialise():
    board=[[],[],[],[],[],[],[],[],[]]
    for i in range(0,9):
        temp=input("Enter row "+str(i+1)+" and enter 0 if blank\n")
        for j in range(0,9):
            if temp[j]!="0":
                board[i].append(int(temp[j]))
            else:
                board[i].append(0)
    for k in range(0,9):
        print("Row: "+str(k+1)+ str(board[k]))
    return np.matrix(board)

#sudoku_board=np.matrix([[0, 0, 6, 1, 0, 2, 5, 0, 0],[0, 0, 0, 0, 0, 0, 1, 4, 0],[0, 0, 0, 0, 4, 0, 0, 0, 0],[9, 0, 2, 0, 3, 0, 4, 0, 1],[0, 8, 0, 0, 0, 0, 0, 7, 0],[1, 0, 3, 0, 6, 0, 8, 0, 9],[0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 5, 4, 0, 0, 0, 9, 1, 0],[0, 0, 7, 5, 0, 3, 2, 0, 0]])
sudoku_board=initialise()

def possible_place(y,x,n):
    global sudoku_board
    for i in range(0,9):
        if sudoku_board[y,i]==n:
            return False
    for j in range(0,9):
        if sudoku_board[j,x]==n:
            return False
    x_0=x-x%3
    y_0=y-y%3
    for r in range(0,3):
        for t in range(0,3):
            if sudoku_board[y_0+r,x_0+t]==n:
                return False
    return True

def empty(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[i,j]==0:
                return True
    return False

def solve():
    global sudoku_board
    for y in range(9):
        for x in range(9):
            if sudoku_board[y,x]==0:
                for n in range(1,10):
                    if possible_place(y,x,n):
                        sudoku_board[y,x]=n
                        solve()
                        sudoku_board[y,x]=0
                return
    if not empty(sudoku_board):
        print(sudoku_board)
    input("More")
    
start=time.time()                   
solve()           
end=time.time()
diff=end-start
print("Time elapsed: "+str(diff)+ "seconds")
