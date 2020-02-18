#Step 1
#display board function
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


#Step 2
#take input from user and assign X or O
#output is in form of tuple
#(Player 1 marker,Player 2 marker) 
def player_input():
    marker=''
    while marker != 'X' and marker != 'O':
        marker =input('Player1: Choose X or O:').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')


#Step 3
#function that takes in board list object 
#assigns 'X' and 'O' to desired position(number 1-9)
#and assigns to board
def place_maker(board,marker,position):
    board[position] = marker


#Step 4
#Win Check i.e check all winning possibilities
#first three conditions for rows
#second three condition for columns
#third two condition for diagonals 
def win_check(board,mark):
  return ((board[1] == mark and board[2] == mark and board[3] == mark) or
  (board[4] == mark and board[5] == mark and board[6] == mark) or
  (board[7] == mark and board[8] == mark and board[9] == mark) or
  (board[1] == mark and board[4] == mark and board[7] == mark) or
  (board[2] == mark and board[5] == mark and board[8] == mark) or
  (board[3] == mark and board[6] == mark and board[9] == mark) or
  (board[1] == mark and board[5] == mark and board[9] == mark) or
  (board[7] == mark and board[5] == mark and board[3] == mark))


#test win check
#print(win_check(test_board,'X'))



#step 5
#random decide which player goes first
import random
def choose_first():
    flip = random.randint(0,1)
    if flip==0:
        return "Player 1"
    else:
        return "Player 2"


#step 6
#return boolean where the space is empty or not in board
def space_check(board,position):
    return board[position] == ' '

#step 7
#board is full or not and reurns bool
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #return true if board is full i.e 
    #comes out of loop
    return True


#step 8
#asks next position and 
#and checks step 6 space_check if its free then\
#position for next use
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position =int(input('Choose Pposition(1-9):'))
    return position


#step 9
#play again asking function
def replay():
    choice=input('Play again? Enter Yes or NO')
    return choice == 'Yes'


#step 10 Final Touch 
#mixing Logic

#while loop to keeping running game
print('Welcome to TIC TAC TOE')
while True:
    #play the game
    
    ## set everything (board,who is first,choose marker X,O)
    the_board = [' ']*10
    player1_marker,player2_marker=player_input()
    
    turn = choose_first()
    print(turn +'will go first')
    play_game= input('Ready to play? y or n:')
    if play_game == 'y':
        game_on=True
    else:
        game_on=False

    ## game play
    while game_on:
        if turn == 'Player 1':
            #show board
            display_board(the_board)
            #choose position
            position=player_choice(the_board)
            #place the marker
            place_maker(the_board,player1_marker,position)
            #check win
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 Won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie Game')
                    game_on=False
                else:
                    turn = 'Player 2'



        else:
           
                #show board
                display_board(the_board)
                #choose position
                position=player_choice(the_board)
                #place the marker
                place_maker(the_board,player2_marker,position)
                #check win
                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print('Player 2 Won')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie Game')
                        game_on=False
                    else:
                        turn = 'Player 1'   
    if not replay():
        break
#break out to the while loop on replay button

