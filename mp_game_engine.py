from components import initialise_board, create_battleships, place_battleships, print_board
from game_engine import cli_coordinates_input, attack
player_board = {
    "Player1": {
        "board": None,  # Store the board for Player 1
        "battleships": None  # Store the battleships for Player 1
    },
    "Player2": {
        "board": None,  # Store the board for Player 2
        "battleships": None  # Store the battleships for Player 2
    }
    
}
from random import randint

def generate_attack(board_size=10):  # Default board_size is 10
    return (randint(0, board_size - 1), randint(0, board_size - 1))





def ai_opponent_game_loop():
    print("Welcome to the Battleship game against AI Opponent!")

    # Initialize players for the user and AI opponent
    players = {
        "User": {
            "board": initialise_board(),
            "battleships": create_battleships()
        },
        "AI Opponent": {
            "board": initialise_board(),
            "battleships": create_battleships()
        }
    }

    # Place battleships using custom placement for the user and random placement for AI
    place_battleships(players["User"]["board"], players["User"]["battleships"], algorithm='custom')
    place_battleships(players["AI Opponent"]["board"], players["AI Opponent"]["battleships"], algorithm='random')


    while any(size > 0 for size in players["User"]["battleships"].values()) and any(size > 0 for size in players["AI Opponent"]["battleships"].values()):
        print("User's Turn:")
        print_board(players["AI Opponent"]["board"])

        # User's turn
        print("Enter coordinates for your attack:")
        user_coordinates = cli_coordinates_input()
        user_hit = attack(user_coordinates, players["AI Opponent"]["board"], players["AI Opponent"]["battleships"])
        if user_hit:
            print("You hit a battleship!")
        else:
            print("You missed.")
        #AI's Turn
        print("AI Opponent's Turn:")
        ai_attack = generate_attack(len(players["User"]["board"]))
        ai_hit = attack(ai_attack, players["User"]["board"], players["User"]["battleships"])
        print("AI Opponent's Attack Coordinates:", ai_attack)
        if ai_hit:
            print("AI Opponent hit your battleship!")
        else:
            print("AI Opponent missed.")

    if all(size == 0 for size in players["User"]["battleships"].values()):
        print("Congratulations! You've won!")
    else:
        print("AI Opponent won! Better luck next time.")

if __name__ == "__main__":
    ai_opponent_game_loop()  
