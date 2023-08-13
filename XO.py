import sys
import os

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
  
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
# Clear the terminal screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
while True:
    # Game board initialization
    cell_1 = ' '
    cell_2 = ' '
    cell_3 = ' '
    cell_4 = ' '
    cell_5 = ' '
    cell_6 = ' '
    cell_7 = ' '
    cell_8 = ' '
    cell_9 = ' '
    #Print board
    def print_board():
        print( cell_1, "|", cell_2, "|", cell_3)
        print("---------")
        print( cell_4, "|", cell_5, "|", cell_6)
        print("---------")
        print(cell_7, "|", cell_8, "|", cell_9)
    # Play game
    while True:
        turn = True
        for i in range(9):
            if i % 2 == 0:
                player = 'X'
            else:
                player = 'O'
            if turn==False:
                if player=='X':
                    player = 'O'
                elif player=='O':
                    player = 'X'
            while True:
                try:
                    prPurple("Enter a number between 1-9: ")
                    x = int(input())
                    if x < 1 or x > 9:
                        prRed("Invalid number. Try again.")
                    else:
                        break
                except ValueError:
                    prRed("Invalid input. Enter a number between 1-9!")
            if x == 1 and cell_1 == ' ':
                cell_1 = player
            elif x == 2 and cell_2 == ' ':
                cell_2 = player
            elif x == 3 and cell_3 == ' ':
                cell_3 = player
            elif x == 4 and cell_4 == ' ':
                cell_4 = player
            elif x == 5 and cell_5 == ' ':
                cell_5 = player
            elif x == 6 and cell_6 == ' ':
                cell_6 = player
            elif x == 7 and cell_7 == ' ':
                cell_7 = player
            elif x == 8 and cell_8 == ' ':
                cell_8 = player
            elif x == 9 and cell_9 == ' ':
                cell_9 = player
            elif cell_1 != ' ' or cell_2 != ' ' or cell_3 != ' ' or \
                    cell_4 != ' ' or cell_5 != ' ' or cell_6 != ' ' or \
                    cell_7 != ' ' or cell_8 != ' ' or cell_9 != ' ':
                prRed('This cell is full. Try another number.')
                if player == 'O' and turn:
                    turn = False
                elif player == 'X' and not turn:
                    turn = True
                continue
            clear_screen()
            print_board()
            # Check winner
            if (cell_1 == cell_2 == cell_3 == player) or \
                    (cell_4 == cell_5 == cell_6 == player) or \
                    (cell_7 == cell_8 == cell_9 == player) or \
                    (cell_1 == cell_4 == cell_7 == player) or \
                    (cell_2 == cell_5 == cell_8 == player) or \
                    (cell_1 == cell_5 == cell_9 == player) or \
                    (cell_3 == cell_5 == cell_7 == player) or \
                    (cell_3 == cell_6 == cell_9 == player):
                prGreen(f"{player} player wins!!!")
                break
        # Play again
        prYellow("Do you want to play again? (yes/no)")
        answer = input()
        if answer== 'yes':
            break
        elif answer == 'no' :
            clear_screen()
            prYellow("Thank you for playing!")
            exit()
        else:
            clear_screen()
            prRed("Invalid input. Exiting the game.")
            exit()