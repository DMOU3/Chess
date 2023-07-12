#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:00:01 2023

@author: dennismou
"""

print("Hello this is my chess file") 
print()

# in the terminal, navigate to the correct directory. 
# git add file_name.py IF it is a new file
# git commit -m "my message here"
# git push

#from defs import *
#from printing import *


whites = {'King': u'\u2654','Queen':u'\u2655',
          'Rook':u'\u2656','Bishop':u'\u2657',
          'Knight':u'\u2658','Pawn':u'\u2659'}
blacks = {'King': u'\u265A','Queen':u'\u265B',
          'Rook': u'\u265C','Bishop':u'\u265D',
          'Knight':u'\u265E','Pawn': u'\u265F'}
alph = {'a':0,'b':1,'c':2,'d':3,
        'e':4,'f':5,'g':6,'h':7}

board_dim = 8

def init_board():
    # r = []
    # c = []
    # for i in range(board_dim):
    #     r.append("_")
    b = [["_" for j in range(board_dim)] for _ in range(board_dim)]
    for k in range(board_dim):
        b[1][k] = blacks['Pawn']
        b[6][k] = whites['Pawn']
    
    b[0][0] = b[0][7] = blacks['Rook']   
    b[7][0] = b[7][7] = whites['Rook']
    
    b[0][1] = b[0][6] = blacks['Knight']   
    b[7][1] = b[7][6] = whites['Knight']
    
    b[0][2] = b[0][5] = blacks['Bishop']   
    b[7][2] = b[7][5] = whites['Bishop']
    
    b[0][3] = blacks['King']   
    b[7][3] = whites['King']
  
    b[0][4] = blacks['Queen']   
    b[7][4] = whites['Queen']
  
    return b

def print_board(board):
    print("  ", end= "")
    for i in range(len(board)):
        print(list(alph.keys())[i], end = " ")
    print()
    for i in range(len(board)):
        print(board_dim-i, end = " ")
        for j in range(len(board[i])):
            pass
            print(board[i][j], end = " ")
        print()

def main():
    board = init_board()
    player_turn = "Whites"
    t = 0
    while t < 3:
        t += 1
        print()
        print(player_turn,"Turn!")
        print_board(board)
        print()
        board = move_piece(board)
        
        
    
        if player_turn == "Whites":
            player_turn = "Blacks"
        else:
            player_turn = "Whites"

def move_piece(board):
    s_letter = str(input("Enter the Column of Start: "))
    s_num = 8 - int(input("Enter the Row of Start: "))
    f_letter = str(input("Enter the Column of Finish: "))
    f_num = 8 - int(input("Enter the Row of Finish: "))
    board[f_num][alph[f_letter]] = board[s_num][alph[s_letter]]
    board[s_num][alph[s_letter]] = "_"
    
    return board


if __name__ == "__main__":
    main()