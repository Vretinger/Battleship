import board
import os

HIT = " X "
MISS = " O "
EMPTY = "   "
SHIP = " # "
NPC_SHIP = "   "

npc = board.Board((11, 11))
player = board.Board((11, 11))


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

    while not ship_valid:
        ship_direction = input('Enter your ship direction "UP, DOWN, LEFT, RIGHT"\n').upper()

        if ship_direction == "UP":
            # Check if all spots from (x, y-size) to (x, y-1) are not occupied
            if all((x, y-i) not in player for i in range(1, size)):
                for i in range(1, size + 1):
                    player[x, y-i] = SHIP
                ship_valid = True
            else:
                print("Error: Ship placement is out of bounds or overlaps another ship")

        elif ship_direction == "DOWN":
            # Check if all spots from (x, y+1) to (x, y+size) are not occupied
            if all((x, y+i) not in player for i in range(1, size)):
                for i in range(1, size + 1):
                    player[x, y+i] = SHIP
                ship_valid = True
            else:
                print("Error: Ship placement is out of bounds or overlaps another ship")

        elif ship_direction == "LEFT":
            # Check if all spots from (x-size, y) to (x-1, y) are not occupied
            if all((x-i, y) not in player for i in range(1, size)):
                for i in range(1, size + 1):
                    player[x-i, y] = SHIP
                ship_valid = True
            else:
                print("Error: Ship placement is out of bounds or overlaps another ship")

        elif ship_direction == "RIGHT":
            # Check if all spots from (x+1, y) to (x+size, y) are not occupied
            if all((x+i, y) not in player for i in range(1, size)):
                for i in range(1, size + 1):
                    player[x+i, y] = SHIP
                ship_valid = True
            else:
                print("Error: Ship placement is out of bounds or overlaps another ship")

        else:
            print("Invalid direction")
    clear()
    draw_boards()


def draw_boards():
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