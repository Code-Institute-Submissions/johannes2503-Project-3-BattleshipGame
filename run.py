# BattleShip Game

import random

def build_board(levels):
    return [["." for count in range(levels)] for count in range(levels)]

def generate_board(board):
    for b in board:
        print(*b)


def build_ship(levels):

    len_ship = random.randint(2, levels)
    orientation = random.randint(0, 1)

    if orientation == 0:
        row_ship = [random.randint(0, levels - 1) * len_ship]
        col = random.randint(0, levels - len_ship)
        col_ship = list(range(col, col + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    else:
        col_ship = [random.randint(0, levels - 1)] * len_ship
        row = random.randint(0, levels - len_ship)
        row_ship = list(range(row, row + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)


def user_level_choice():
    true = True
    while true == True:
        try:
            print("Choose your Level between 1-3 (1 = grid of 5  2 = grid of 7 and 3 = grid of 10):")
            level = int(input("Level:"))
            if level == 1:
                print("You chose level 1")
                levels = level * 5
                return levels
            elif level == 2:
                print("You chose level 2")
                levels = level * 3
                return levels
            elif level == 3:
                print("You chose level 3")
                levels = level * 3
                return levels
            else: 
                level != (1,2,3)
                print("Not valid level!")  

        except ValueError:
                print("Incorrect input, must be a integer between 1-3")

def user_guess():
    row = int(input("Row: ")) -1
    col = int(input("Col ")) -1
    return (row, col)

def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print("You have already guessed that, guess again!")
        return board
    guesses.append(guess)
    if guess in ship:
        print("You srhot my battleship")
        board[guess[0]][guess[1]] = "X"
        ship.remove(guess)
        return board
    print("You missed!")
    return board

def welcome_message():
    print('Welcome to Battleship!')
    print('There is a battleship hidden in this board. Enter your row and column guesses to sink it!')



def main():
    welcome_message()
    levels = user_level_choice()
    board = build_board(levels)
    ship = build_ship(levels)
    guesses = []
    while len(ship) > 0:
        board = update_board(user_guess(), board, ship, guesses)
        generate_board(board)
    print('You sunk my battleship!')
    return
   
main()
        


