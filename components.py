def initialise_board(size=10):
    return [[None for _ in range(size)] for _ in range(size)]

new_board = initialise_board(size=10)
print( "New Board = ",new_board)
def create_battleships(filename="battleships.txt"):
    battleships = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                name, size = line.strip().split(':')
                battleships[name.strip()] = int(size.strip())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    return battleships
ships_info = create_battleships()
print("Ships =",ships_info)
from random import randint
def place_battleships(board, ships):
    for ship_name, ship_size in ships.items():
        placed = False
        while not placed:
            direction = randint(0, 1)  
            if direction == 0:
                row = randint(0, len(board) - 1)
                col = randint(0, len(board) - ship_size)
                if all(board[row][col + i] is None for i in range(ship_size)):
                    for i in range(ship_size):
                        board[row][col + i] = ship_name
                    placed = True
            else:
                row = randint(0, len(board) - ship_size)
                col = randint(0, len(board) - 1)
                if all(board[row + i][col] is None for i in range(ship_size)):
                    for i in range(ship_size):
                        board[row + i][col] = ship_name
                    placed = True
    return board
board_size = 10  
my_board = initialise_board(board_size)
my_ships = create_battleships()


updated_board = place_battleships(my_board, my_ships)

from random import randint
import json

def place_battleships(board, ships, placement_file='placement.json', algorithm='random'):
    if algorithm == 'custom':
        try:
            with open(placement_file, 'r') as file:
                placements = json.load(file)
                for ship_name, data in placements.items():
                    row = int(data[0])
                    col = int(data[1])
                    orientation = data[2]

                    if orientation == 'h':
                        for i in range(ships[ship_name]):
                            board[row][col + i] = ship_name
                    elif orientation == 'v':
                        for i in range(ships[ship_name]):
                            board[row + i][col] = ship_name
        except FileNotFoundError:
            print(f"Placement file '{placement_file}' not found.")
    elif algorithm == 'random':
        for ship_name, ship_size in ships.items():
            placed = False
            while not placed:
                direction = randint(0, 1)  
                if direction == 0:
                    row = randint(0, len(board) - 1)
                    col = randint(0, len(board) - ship_size)
                    if all(board[row][col + i] is None for i in range(ship_size)):
                        for i in range(ship_size):
                            board[row][col + i] = ship_name
                        placed = True
                else:
                    row = randint(0, len(board) - ship_size)
                    col = randint(0, len(board) - 1)
                    if all(board[row + i][col] is None for i in range(ship_size)):
                        for i in range(ship_size):
                            board[row + i][col] = ship_name
                        placed = True
    else:
        print("Invalid algorithm specified.")

    return board



def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell is not None else 'O' for cell in row))
