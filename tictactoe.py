#Initialisation
import os

player1 = None
player2 = None
first_time = True
counter = 0
flag = 0
board = [0,1,2,3,4,5,6,7,8,9,0]

def input_player_marker():
    global player1
    player1 = input("Player 1 please pick your marker ['X' or 'O'] :")
    print("Player 2 gets to go first! Good Luck :)")
    assign_marker(player1)

def assign_marker(player1):
    global player2
    if(player1 == 'X'):
        player2 = 'O'
    elif(player1 == 'O'):
        player2 = 'X'
    else:
        print('Entry is neither X nor O!')
        input_player_marker()
    display_board()

def display_board():
    global first_time
    if(first_time==True):
        print('The board is as follows')
    else:
        print('Updated board is as follows')
    for i in range(1,10):
        if(i%3==0):
            print(board[i], end='\n')
        else:
            print(board[i], end=' | ')
    first_time = False

def take_input():
    global player1, player2, counter
    entry = None
    if(counter % 2) == 0:
        position = int(input('Player 2, Enter the position where you with to enter your marker. Choose wisely!'))
        if(check(position) == True):
            entry = player2
            counter += 1
    else:
        position = int(input('Player 1, Enter the position where you with to enter your marker. Choose wisely!'))
        if(check(position) == True):
            entry = player1
            counter += 1
    update_board(position, entry)

def check(position):
    if(board[position]=='X' or board[position]=='O'):
        return False
    else:
        return True

def update_board(position, entry):
    global flag
    flag = flag + 1
    board[position] = entry
    display_board()
    if(check_winner() == 'X Wins'):
        print('X Wins')
        again = input('Want to play again ? Y/N')
        if(again == 'Y'):
            clear_board()
            input_player_marker()
            take_input()
        elif(again == 'N'):
            print('Thank you for playing!')
    elif(check_winner() == 'O Wins'):
        print('O Wins')
        again = input('Want to play again ? Y/N')
        if(again == 'Y'):
            clear_board()
            input_player_marker()
            take_input()
        elif(again == 'N'):
            print('Thank you for playing!')
    elif(flag == 9):
        print("It's a tie")
        again = input('Want to play again ? Y/N')
        if(again == 'Y'):
            clear_board()
            input_player_marker()
            take_input()
        elif(again == 'N'):
            print('Thank you for playing!')
    else:
        take_input()

def check_winner():
    global board
    #X Win Conditions
    if(board[1] == 'X' and board[2] == 'X' and board[3] == 'X'):
        return 'X Wins'
    elif(board[4] == 'X' and board[5] == 'X' and board[6] == 'X'):
        return 'X Wins'
    elif(board[7] == 'X' and board[8] == 'X' and board[9] == 'X'):
        return 'X Wins'
    elif(board[1] == 'X' and board[4] == 'X' and board[7] == 'X'):
        return 'X Wins'
    elif(board[2] == 'X' and board[5] == 'X' and board[8] == 'X'):
        return 'X Wins'
    elif(board[3] == 'X' and board[6] == 'X' and board[9] == 'X'):
        return 'X Wins'
    elif(board[1] == 'X' and board[5] == 'X' and board[9] == 'X'):
        return 'X Wins'
    elif(board[3] == 'X' and board[5] == 'X' and board[7] == 'X'):
        return 'X Wins'
    #O Win Conditions
    elif(board[1] == 'O' and board[2] == 'O' and board[3] == 'O'):
        return 'O Wins'
    elif(board[4] == 'O' and board[5] == 'O' and board[6] == 'O'):
        return 'O Wins'
    elif(board[7] == 'O' and board[8] == 'O' and board[9] == 'O'):
        return 'O Wins'
    elif(board[1] == 'O' and board[4] == 'O' and board[7] == 'O'):
        return 'O Wins'
    elif(board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return 'O Wins'
    elif(board[3] == 'O' and board[6] == 'O' and board[9] == 'O'):
        return 'O Wins'
    elif(board[1] == 'O' and board[5] == 'O' and board[9] == 'O'):
        return 'O Wins'
    elif(board[3] == 'O' and board[5] == 'O' and board[7] == 'O'):
        return 'O Wins'
    else:
        return False

def clear_board():
    global board
    os.system('clear')
    board = [0,1,2,3,4,5,6,7,8,9,0]
