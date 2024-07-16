import board
import os
import random
import sys

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
    if y == 0:
        y = 10

    return x, y


def is_valid_input(ship_input):
    if ship_input.upper() == "EXIT":
        sys.exit("Game exited by user.")
    if not len(ship_input) == 2:
        return False
    if not ship_input[1:].isdigit():
        return False
    if not ('A' <= ship_input[0] <= 'J'):
        return False

    x, y = get_coordinates(ship_input)
    return (x, y) in player
    
    
def place_ships(name, size):
    ship_valid = False
    while not ship_valid:
        ship_input = input(f'Enter your {name}({size}) start location. E.g."H5"\n').upper()
        if not is_valid_input(ship_input):
            print("Invalid input. Please enter a letter followed by a number within the board range.")
            continue
        x, y = get_coordinates(ship_input)
        if player[(x, y)] != EMPTY:
            print(player[(x, y)])
            print("Starting position already occupied. Choose a different location.")
            continue
        player[x, y] = SHIP
        clear()
        draw_boards()
    
        while not ship_valid:
            ship_direction = input('Enter your ship direction "UP, DOWN, LEFT, RIGHT"\n').upper()
            if ship_direction == "UP":
                if (x, y-size) in player:
                    if all((x, y-i) not in player or player[(x, y-i)] == EMPTY for i in range(1, size)):
                        for i in range(1, size):
                            player[x, y-i] = SHIP    
                        ship_valid = True
                    else:
                        print("Error: Ship placement is overlapping")
                else:
                    print("Error: Ship placement is out of bounds")
            elif ship_direction == "DOWN":
                if (x, y+size) in player:
                    if all((x, y+i) not in player or player[(x, y+i)] == EMPTY for i in range(1, size)):
                        for i in range(1, size):
                            player[x, y+i] = SHIP
                        ship_valid = True
                    else:
                        print("Error: Ship placement is overlapping")
                else:
                    print("Error: Ship placement is out of bounds")
            elif ship_direction == "LEFT":
                if (x-size, y) in player:
                    if all((x-i, y) not in player or player[(x-i, y)] == EMPTY for i in range(1, size)):
                        for i in range(1, size):
                            player[x-i, y] = SHIP
                        ship_valid = True
                    else:
                        print("Error: Ship placement is overlapping")
                else:
                    print("Error: Ship placement is out of bounds")
            elif ship_direction == "RIGHT":
                if (x+size, y) in player:
                    if all((x+i, y) not in player or player[(x+i, y)] == EMPTY for i in range(1, size)):
                        for i in range(1, size):
                            player[x+i, y] = SHIP
                        ship_valid = True
                    else:
                        print("Error: Ship placement is overlapping")
                else:
                    print("Error: Ship placement is out of bounds")
            else:
                print("Invalid direction")
    clear()
    draw_boards()


def place_ships_randomly(name, size):
    ship_valid = False

    while not ship_valid:
        # Generate random starting position
        x = random.randint(1, 11)
        y = random.randint(1, 11)
        # Randomly choose a direction
        ship_direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        
        if ship_direction == "UP":
            if (x, y-size) in npc:
                print(x, y-size)
                if all(npc[(x, y - i)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        npc[(x, y - i)] = SHIP
                    ship_valid = True

        elif ship_direction == "DOWN":
            if (x, y+size) in npc:
                print(x, y+size)
                if all(npc[(x, y + i)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        npc[(x, y + i)] = SHIP
                    ship_valid = True

        elif ship_direction == "LEFT":
            if (x-size, y) in npc:
                print(x-size, y)
                if all(npc[(x - i, y)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        npc[(x - i, y)] = SHIP
                    ship_valid = True

        elif ship_direction == "RIGHT":
            if (x+size, y) in npc:
                print(x+size, y)
                if all(npc[(x + i, y)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        npc[(x + i, y)] = SHIP
                    ship_valid = True
    clear()
    draw_boards()


def draw_boards():
    ship_sizes.draw(use_borders=False)
    print("₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪ COMPUTER'S BOARD ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
    npc.draw()
    print("\n₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪ PLAYER'S BOARD ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
    player.draw()


def players_turn():
    attack_valid = False
    while not attack_valid:
        ship_input = input(f'Enter your the location of your attack! E.g."H5"\n').upper()
        if not is_valid_input(ship_input):
            print("Invalid input. Please enter a letter followed by a number within the board range.")
            continue
        x, y = get_coordinates(ship_input)
        if npc[(x, y)] == EMPTY:
            npc[(x, y)] = MISS
            clear()
            draw_boards()
            print("You missed!")
            attack_valid = True
        elif npc[(x, y)] == SHIP:
            npc[(x, y)] = HIT
            clear()
            draw_boards()
            print("You hit! Attack again")
        else:    
            print("You have already guessed that location. Choose a different location.")
            


def game_play():
    game_finished = False
    won = False
    while not game_finished:
        print("Player's turn!")
        players_turn()
        if won == True:
            game_over("player")
            game_finished = True
        print("Computer's turn!")
        npc_turn()
        if won == True:
            game_over("npc")
            game_finished = True


def game_over(winner):
    if winner == "player":
        print("Player won")

    elif winner == "npc":
        print("Computer won")

def game_start():
    place_ships_randomly("Carrier", 6)
    place_ships_randomly("Battleship", 5)
    place_ships_randomly("Destroyer", 4)
    place_ships_randomly("Submarine", 4)
    place_ships_randomly("Patrol Boat", 3)
    #place_ships("Carrier", 5)
    #place_ships("Battleship", 4)
    #place_ships("Destroyer", 3)
    #place_ships("Submarine", 3)
    #place_ships("Patrol Boat", 2)
    game_play()

def main():
    create_board(npc)
    create_board(player)
    draw_boards()
    game_start()


main()