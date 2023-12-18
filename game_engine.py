from components import initialise_board, create_battleships, place_battleships, print_board

def attack(coordinates, board, battleships):
    row, col = coordinates
    target = board[row][col]

    if target is not None:
        
        print("Hit!")
        board[row][col] = None  

        
        battleships[target] -= 1
        if battleships[target] == 0:
            print(f"You sunk the {target}!")
        return True
    else:
        
        print("Miss!")
        return False

def cli_coordinates_input():
    while True:
        try:
            x = int(input("Enter the x-coordinate (0 to 9): "))
            y = int(input("Enter the y-coordinate (0 to 9): "))
            if 0 <= x <= 9 and 0 <= y <= 9:
                return x, y
            else:
                print("Coordinates should be in the range of 0 to 9.")
        except ValueError:
            print("Please enter valid integer coordinates.")


def simple_game_loop():
    print("Welcome to the Battleship game!")

    
    board = initialise_board()
    ships = create_battleships()
    place_battleships(board, ships)

    while any(size > 0 for size in ships.values()):
        print_board(board)  

        
        print("Enter coordinates for your attack:")
        coordinates = cli_coordinates_input()

        
        hit = attack(coordinates, board, ships)
        if hit:
            print("You hit a battleship!")
        else:
            print("You missed.")

    print("Congratulations! You've sunk all battleships!")
    print("Game Over")

if __name__ == "__main__":
    simple_game_loop()  
