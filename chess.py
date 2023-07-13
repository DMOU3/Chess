#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:00:01 2023

@author: dennismou
"""

print("Hello, this is my chess file.") 

# in the terminal, navigate to the correct directory. 
# git add file_name.py IF it is a new file
# git status
# git commit -m "my message here"
# git push



whites = {'King': u'\u2654','Queen':u'\u2655',
          'Rook':u'\u2656','Bishop':u'\u2657',
          'Knight':u'\u2658','Pawn':u'\u2659'}
blacks = {'King': u'\u265A','Queen':u'\u265B',
          'Rook': u'\u265C','Bishop':u'\u265D',
          'Knight':u'\u265E','Pawn': u'\u265F'}
alph = {'a':0,'b':1,'c':2,'d':3,
        'e':4,'f':5,'g':6,'h':7}

board_dim = 8
board_design = "◻️"

def init_board():
    # r = []
    # c = []
    # for i in range(board_dim):
    #     r.append("_")
    b = [[board_design for j in range(board_dim)] for _ in range(board_dim)]
    
    for k in range(board_dim):
        b[1][k] = blacks['Pawn']
        b[6][k] = whites['Pawn']
    
    b[0][0] = b[0][7] = blacks['Rook']   
    b[7][0] = b[7][7] = whites['Rook']
    
    b[0][1] = b[0][6] = blacks['Knight']   
    b[7][1] = b[7][6] = whites['Knight']
    
    b[0][2] = b[0][5] = blacks['Bishop']   
    b[7][2] = b[7][5] = whites['Bishop']
    
    b[0][4] = blacks['King']   
    b[7][4] = whites['King']
  
    b[0][3] = blacks['Queen']   
    b[7][3] = whites['Queen']
  
    return b

def print_board(board):
    print("  ", end= "")
    for i in range(len(board)):
        print(list(alph.keys())[i], end = " ")
    print()
    for i in range(len(board)):
        print(board_dim-i, end = " ")
        for j in range(len(board[i])):
            # pass
            print(board[i][j], end = " ")
        print()

def main():
    board = init_board()
    t=0
    player_turn = "Whites"
    
    while True:
        
        print()
        print(player_turn,"Turn!")
        print_board(board)
        print()
        board = move_piece(board, player_turn)
        if check_vic(board) == None:
            pass
        else:
            print(check_vic(board))
            print_board(board)
            break
        t += 1
        if player_turn == "Whites":
            player_turn = "Blacks"
        else:
            player_turn = "Whites"
        

def move_piece(board, player_turn):
    s_letter = str(input("Enter the Column of Start: "))
    s_num = 8 - int(input("Enter the Row of Start: "))
    print()
    correct_pick(board,player_turn,s_letter,s_num)
    
    f_letter = str(input("Enter the Column of Finish: "))
    f_num = 8 - int(input("Enter the Row of Finish: "))
    if s_letter == f_letter and s_num == f_num:
        print("You need to make a move ... LOL")
        print()
        return move_piece(board, player_turn)
    print()
    fdly_fire(board,player_turn,s_letter,s_num,f_letter,f_num)
    
    p = board[s_num][alph[s_letter]]
    if p == '♔' or p == '♚':
        # King
        king(board, player_turn, s_letter, s_num, f_letter, f_num)
    elif p == '♕' or p == '♕':
        # Queen
        queen(board, player_turn, s_letter, s_num, f_letter, f_num)
    elif p == '♖' or p == '♜':
        # Rook
        rook(board, player_turn, s_letter, s_num, f_letter, f_num)
    elif p == '♗' or p == '♝':
        #  Bishop
        bishop(board, player_turn, s_letter, s_num, f_letter, f_num)
    elif p == '♘' or p == '♘':
        # Knight
        pass
    elif p == '♟' or p == '♙':
        # Pawn
        pass
    else:
        pass
    
    board[f_num][alph[f_letter]] = board[s_num][alph[s_letter]]
    board[s_num][alph[s_letter]] = board_design
    return board

def correct_pick(board,player_turn,s_letter,s_num):
    if player_turn == "Whites" \
        and board[s_num][alph[s_letter]] in blacks.values():
        print("Wrong Piece: You are Whites.")
        return move_piece(board, player_turn)
    elif player_turn == "Blacks" \
            and board[s_num][alph[s_letter]] in whites.values():
        print("Wrong Piece: You are Blacks.")
        return move_piece(board, player_turn)
    else:
        pass

def fdly_fire(board,player_turn,s_letter,s_num,f_letter,f_num):
    if board[s_num][alph[s_letter]] in whites.values() \
            and board[f_num][alph[f_letter]] in whites.values():
        print("Invalid Move: Cannot take your own piece.")
        return move_piece(board, player_turn)
    elif board[s_num][alph[s_letter]] in blacks.values() \
            and board[f_num][alph[f_letter]] in blacks.values():
        print("Invalid Move: Cannot take your own piece.")
        return move_piece(board, player_turn)
    else:
        pass

def king(board, player_turn,s_letter,s_num,f_letter,f_num):
    """ King moves one square in any direction."""
    a = abs(s_num - f_num)
    b = abs(alph.get(s_letter) - alph.get(f_letter))
    if a > 1 or b > 1:
        print("Invalid Move: King moves one square.")
        return move_piece(board, player_turn)

def queen(board, player_turn,s_letter,s_num,f_letter,f_num):
    """ Queen moves in a file or rank or diagonlly but it cannot leap."""
    d1 = abs(s_num - f_num)
    d2 = abs(alph.get(s_letter) - alph.get(f_letter))
    d3 = min(s_num,f_num)
    d4 = max(s_num,f_num)
    d5 = min(alph.get(s_letter),alph.get(f_letter))
    d6 = max(alph.get(s_letter),alph.get(f_letter))
    d7 = min(s_num,f_num)
    d8 = max(s_num,f_num)
    r = d1 / d2

    if r == 1 or r == 0:
        pass
    elif 1/r == 0:
        pass
    else:
        print("Invalid Move: Queen moves a file, rank or diagonlly.")
        return move_piece(board, player_turn)
    if d1 == d2:
        for i in range(d3+1,d4):
            if board[i][i] != board_design:
                print("Invalid Move: Queen cannot leap.")
                return move_piece(board, player_turn)
    elif s_num == f_num:
        for i in range(d5+1,d6):
            if board[s_num][i] != board_design:
                print("Invalid Move: Queen cannot leap.")
                return move_piece(board, player_turn)
    elif s_letter == f_letter:
        for i in range(d7+1,d8):
            if board[i][alph.get(s_letter)] != board_design:
                print("Invalid Move: Queen cannot leap.")
                return move_piece(board, player_turn)

def rook(board, player_turn,s_letter,s_num,f_letter,f_num):
    """Rook moves in single file or rank, but it cannot leap."""
    if s_num != f_num and s_letter != f_letter:
        print("Invalid Move: Rook moves in a file or rank.")
        return move_piece(board, player_turn)
    elif s_num == f_num:
        a = min(alph.get(s_letter),alph.get(f_letter))
        b = max(alph.get(s_letter),alph.get(f_letter))
        for i in range(a+1,b):
            if board[s_num][i] != board_design:
                print("Invalid Move: Rook cannot leap.")
                return move_piece(board, player_turn)
    elif s_letter == f_letter:
        a = min(s_num,f_num)
        b = max(s_num,f_num)
        for i in range(a+1,b):
            if board[i][alph.get(s_letter)] != board_design:
                print("Invalid Move: Rook cannot leap.")
                return move_piece(board, player_turn)

def bishop(board, player_turn, s_letter, s_num, f_letter, f_num):
    """Bishop moves diagonally and cannot leap."""
    a = abs(s_num - f_num)
    b = abs(alph.get(s_letter) - alph.get(f_letter))
    c = min(s_num,f_num)
    d = max(s_num,f_num)
    if a != b:
        print("Invalid Move: Bishop moves diagonally.")
        return move_piece(board, player_turn)
    else:
        for i in range(c+1,d):
            if board[i][i] != board_design:
                print("Invalid Move: Bishop cannot leap.")
                return move_piece(board, player_turn)

def check_vic(board):
    c_1 = 0
    c_2 = 0
    for i in board:
        if whites['King'] in i:
            c_1 += 1
        if blacks['King'] in i:
            c_2 += 1

    if c_1 > c_2:
        return 'Whites Win!!!'
    elif c_1 < c_2:
        return 'Blacks Win!!!'
    else:
        pass


if __name__ == "__main__":
    main()