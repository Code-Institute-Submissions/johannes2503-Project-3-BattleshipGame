# BattleShip Game

import random

# Function to build layout of boards


def build_board(levels):
    return [["." for count in range(levels)] for count in range(levels)]

# Function to generate the computers board


def generate_computer_board(player_board):
    print("Player Board")
    for b in player_board:
        print(*b)

# Function to generate the players board


def generate_player_board(computer_board):
    print("Computer Board")
    for b in computer_board:
        print(*b)

# Function to generate the players ships


def build_player_ship(levels):

    len_ship = random.randint(2, 4)
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

# Function to generate the computers ships


def build_computer_ship(levels):

    comp_len_ship = random.randint(2, 4)
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
    return list(computer_coords)

# Function to get players level choice


def user_level_choice():
    while True:
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
                level != (1, 2, 3)
                print("Not valid level!")

        except ValueError:
                print("Incorrect input, must be a number between 1-3")

# Function to get players row and column guesses


def user_guess(levels):
    while True:
        try:
            row = int(input("Row: ")) - 1
            col = int(input("Col: ")) - 1
            if row < 0 and col < 0:
                print("Input not a positive number, try again!")
                continue
            if row < levels and col < levels:
                    return (row, col)
            else:
                print(f"Incorrect input, must be between 1 and {levels}") 
        except ValueError:
            print("Incorrect input, ")
            print(f"must be a number between 1 and {levels}")

# Function to generate the computers choices


def computer_guess(levels):
    comp_row = random.randint(0, levels) - 1
    comp_col = random.randint(0, levels) - 1
    return (comp_row, comp_col)

# Function to update the computers board with results of player choices


def update_computer_board(player_guess, player_board, player_ship, player_guesses):
    if player_guess in player_guesses:
        return player_board
    player_guesses.append(player_guess)
    if player_guess in player_ship:
        print("computer hit my battleship")
        player_board[player_guess[0]][player_guess[1]] = "X"
        player_ship.remove(player_guess)
        return player_board
    print("The computer missed!")
    player_board[player_guess[0]][player_guess[1]] = "$"
    return player_board

# Function to update the players boardd with computer random generated choices


def update_player_board(computer_guess, computer_board, computer_ship, computer_guesses):
    if computer_guess in computer_guesses:
        print("You have already guessed that, guess again!")
        return computer_board
    computer_guesses.append(computer_guess)
    if computer_guess in computer_ship:
        print("You hit the computers battleship")
        computer_board[computer_guess[0]][computer_guess[1]] = "X"
        computer_ship.remove(computer_guess)
        return computer_board
    print("You missed hiahh!")
    computer_board[computer_guess[0]][computer_guess[1]] = "@"
    return computer_board

# Function with welcome message and start of the game


def welcome_message():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("X                        X")
    print("X                        X")
    print("X Welcome to Battleship! X")
    print("X                        X")
    print("X                        X")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXX\n")

    name = input("What is your name: ")
    print("\n")
    print(f"Hello {name}, there is a battleship hidden on this board.")
    print("\n")
    print("First choose your level then enter your row and column guesses to try and sink it!")
    print("\n")
    print("Choose your Level between 1-3 (1 = grid of 5  2 = grid of 8 and 3 = grid of 12):")

# Function to let the player try again or quit the game


def try_again():
    play_again = True
    while play_again == True:
        try_again = input("Try again? y/n: ")
        if try_again == "y":
            play_again = False
            main()
        elif try_again == "n":
            play_again = False
            exit()
        else:
            print("You must enter y or n!")


# Main function to play the game

def main():
    round = 0
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
        if round > 4:
            print("Game Over no one won...")
            try_again()
        else:
            round += 1
            print(f"Round: {round}")
        player_board = update_player_board(user_guess(levels), player_board, player_ship, player_guesses)
        generate_player_board(player_board)
        computer_board = update_computer_board(computer_guess(levels), computer_board, computer_ship, computer_guesses)
        generate_computer_board(computer_board)
    print("You Won!")
    try_again()

# Calling the main function


main()
