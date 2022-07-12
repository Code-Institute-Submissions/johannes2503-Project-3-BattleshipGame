# BattleShip Game

import random

def build_board(levels):
    return [["." for count in range(levels)] for count in range(levels)]

def generate_player_board(player_board):
    print("Player Board")
    for b in player_board:
       print(*b)
    

def generate_computer_board(computer_board):
    print("Computer Board")
    for b in computer_board:
        print(*b)


def build_player_ship(levels):

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

def build_computer_ship(levels):

    comp_len_ship = random.randint(2, levels)
    comp_orientation = random.randint(0, 1)

    if comp_orientation == 0:
        comp_row_ship = [random.randint(0, levels - 1) * comp_len_ship]
        comp_col = random.randint(0, levels - comp_len_ship)
        comp_col_ship = list(range(comp_col, comp_col + comp_len_ship))
        computer_coords = tuple(zip(comp_row_ship, comp_col_ship))
        
    else:
        comp_col_ship = [random.randint(0, levels - 1)] * comp_len_ship
        row = random.randint(0, levels - comp_len_ship)
        row_ship = list(range(row, row + comp_len_ship))
        computer_coords = tuple(zip(row_ship, comp_col_ship))
        print(computer_coords)
    return list(computer_coords)
 


def user_level_choice():
    true = True
    while true == True:
        try:
            level = int(input("Level: "))
            if level == 1:
                print("You chose level 1")
                levels = level * 5
                return levels
            elif level == 2:
                print("You chose level 2")
                levels = level * 4
                return levels
            elif level == 3:
                print("You chose level 3")
                levels = level * 4
                return levels
            else: 
                level != (1,2,3)
                print("Not valid level!")  

        except ValueError:
                print("Incorrect input, must be a integer between 1-3")

def user_guess(levels):
    while True:
        try:
            row = int(input("Row: ")) -1
            col = int(input("Col: ")) -1
            if row < levels and col < levels:
                return (row, col)
            else:
                print(f"Incorrect input, must be between 1 and {levels}")

        except ValueError:
                    print(f"Incorrect input, must be a integer between 1 and {levels}")
    

        

def computer_guess(levels):
    comp_row = random.randint(0, levels) -1
    comp_col = random.randint(0, levels) -1
    
    return (comp_row, comp_col)

def update_player_board(player_guess, player_board, player_ship, player_guesses):
    if player_guess in player_guesses:
        print("You have already guessed that, guess again!")
        return player_board
    player_guesses.append(player_guess)
    if player_guess in player_ship:
        print("You shot my battleship")
        player_board[player_guess[0]][player_guess[1]] = "X"
        player_ship.remove(player_guess)
        return player_board
    print("You missed!")
    player_board[player_guess[0]][player_guess[1]] = "$"
    return player_board

def update_computer_board(computer_guess, computer_board, computer_ship, computer_guesses):
    if computer_guess in computer_guesses:
        print("You have already guessed that, guess again!")
        return computer_board
    computer_guesses.append(computer_guess)
    if computer_guess in computer_ship:
        print("You shot the computers battleship")
        computer_board[computer_guess[0]][computer_guess[1]] = "X"
        computer_ship.remove(computer_guess)
        return computer_board
    print("You missed hiahh!")
    computer_board[computer_guess[0]][computer_guess[1]] = "@"
    return computer_board

def welcome_message():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("X                        X")
    print("X                        X")
    print("X Welcome to Battleship! X")
    print("X                        X")
    print("X                        X")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX\n")

    print('There is a battleship hidden on this board.\nFirst choose your level then enter your row and column guesses to sink it!\n')

    print("Choose your Level between 1-3 (1 = grid of 5  2 = grid of 8 and 3 = grid of 12):")


def main():
    welcome_message()
    levels = user_level_choice()
    player_board = build_board(levels)
    computer_board = build_board(levels)
    player_ship = build_player_ship(levels)
    computer_ship = build_computer_ship(levels)
    player_guesses = []
    computer_guesses = []
    generate_player_board(player_board)
    generate_computer_board(computer_board)
    while len(player_ship) > 0 and len(computer_ship) > 0:
        player_board = update_player_board(user_guess(levels), player_board, player_ship, player_guesses)
        generate_player_board(player_board)
        computer_board = update_computer_board(computer_guess(levels), computer_board, computer_ship, computer_guesses)
        generate_computer_board(computer_board)
    print("You Won!")
main()
        


