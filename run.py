import board
import os

HIT = " X "
MISS = " O "
EMPTY = "   "
SHIP = " # "
NPC_SHIP = "   "

ship_list = ["Class of ship:", "Carrier", "Battleship", "Destroyer", "Submarine", "Patrol Boat", "Size:", 5, 4, 3, 3, 2]
ship_sizes = board.Board((2, 6))
npc = board.Board((11, 11))
player = board.Board((11, 11))

ship_sizes.populate(ship_list)


def clear():
    # Check the platform and issue the corresponding command to clear the terminal
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and MacOS
        os.system('clear')


def create_board(user):
    user.populate(" 1234567890")  # Populate the top row with numbers
    user.populate("ABCDEFGHIJ", user.iterline((1, 0), (1, 0)))  # Populate the first column with letters
    for x in range(1, 11):
        for y in range(1, 11):
            user[x, y] = EMPTY  # Fill the rest of the board with EMPTY


def get_coordinates(ship_input):
    # Extract the letter and number from the input
    letter = ship_input[0]
    number = ship_input[1:]
    
    # Convert letter to number
    x = ord(letter)-64
    y = int(number)
    
    return x, y





def place_ships(size):
    ship_input = input('Enter your ship start location. E.g."H5" \n')
    x, y = get_coordinates(ship_input)
    player[x, y] = SHIP
    clear()
    draw_boards()
    ship_valid = False

    def place_ships(size):
        ship_input = input('Enter your ship start location. E.g."H5" \n')
        x, y = get_coordinates(ship_input)
        player[x, y] = SHIP
        print("ship_valid")
        ship_valid = False
        print(ship_valid)

        while not ship_valid:
            ship_direction = input('Enter your ship direction "UP, DOWN, LEFT, RIGHT"\n').upper()
            if ship_direction == "UP":
                y -= size
                if (x, y) in player:
                    player[x, y-1] = SHIP
                    player[x, y-2] = SHIP
                    player[x, y-3] = SHIP
                    player[x, y-4] = SHIP
                    ship_valid = True
                else:
                    print("Error: Ship goes out of bounds")
            elif ship_direction == "DOWN":
                y += size
                if (x, y) in player:
                    player[x, y+1] = SHIP
                    player[x, y+2] = SHIP
                    player[x, y+3] = SHIP
                    player[x, y+4] = SHIP
                    ship_valid = True
                else:
                    print("Error: Ship goes out of bounds")
            elif ship_direction == "LEFT":
                x -= size
                if (x, y) in player:
                    player[x-1, y] = SHIP
                    player[x-2, y] = SHIP
                    player[x-3, y] = SHIP
                    player[x-4, y] = SHIP
                    ship_valid = True
                else:
                    print("Error: Ship goes out of bounds")
            elif ship_direction == "RIGHT":
                x += size
                if (x, y) in player:
                    player[x+1, y] = SHIP
                    player[x+2, y] = SHIP
                    player[x+3, y] = SHIP
                    player[x+4, y] = SHIP
                    ship_valid = True
                else:
                    print("Error: Ship goes out of bounds")
            else:
                print("Invalid direction")


def draw_boards():
    ship_sizes.draw(use_borders=False)
    print("₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪ COMPUTER'S BOARD ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
    npc.draw()
    print("\n₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪ PLAYER'S BOARD ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
    player.draw()


def main():
    create_board(npc)
    create_board(player)
    draw_boards()
    place_ships(5)


main()