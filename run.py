# BattleShip Game


class Board:
    """ 
    Board class
    """
    def __init__(self, name, size, num_ships, type):
        self.name = name
        self.num_ships = num_ships
        self.board = [["." for x in range(size)] for y in range(size)]
        self.type = type
        self.guesses = []
        self.ships = []
         