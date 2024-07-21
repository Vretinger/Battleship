import board
import os
import random
import sys
import time

# Constants for board markers
HIT = " X "
MISS = " O "
EMPTY = " ~ "
SHIP = " # "
NPC_SHIP = " ~ "

# Lists and Variables
potential_targets = []  # List to keep track of potential targets around hits
hit_streak = []  # Variables to track hit streak
attack_direction = None  # None, "HORIZONTAL", or "VERTICAL"
attack_direction_reverse = False  # Flag for attack direction

# Ship details and boards initialization
npc = board.Board((11, 11))
player = board.Board((11, 11))
npc_ship_board = board.Board((11, 11))
player_ship_board = board.Board((11, 11))


# Functions to manage the game
# Clears the terminal screen based on the operating system
def clear():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and MacOS
        os.system('printf "\033c"')  # ANSI escape sequence to clear screen


# Creates and populates the game board
def create_board(user):
    # Populate the top row with numbers and the first column with letters.
    user.populate(" 1234567890")
    user.populate("ABCDEFGHIJ", user.iterline((1, 0), (1, 0)))
    for x in range(1, 11):
        for y in range(1, 11):
            user[x, y] = EMPTY  # Fill the rest of the board with EMPTY


# Converts input coordinates to numerical format
def get_coordinates(ship_input):
    letter = ship_input[0]
    number = ship_input[1:]
    x = ord(letter) - 64
    y = int(number)
    if y == 0:
        y = 10
    return x, y


# Validates the user input for coordinate format
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


# Identifies and marks ship positions on the board
def id_ship(user, ship_board, coord, ship_id):
    if user == npc:
        npc[coord] = NPC_SHIP
    else:
        player[coord] = SHIP
    ship_board[coord] = ship_id


# Places ships on the player's board based on user input
def place_ships(name, size, id):
    ship_valid = False
    while not ship_valid:
        ship_input = input((
            f'Enter your {name}({size}) start location. E.g. "H5"\n'
        )).upper()
        if not is_valid_input(ship_input):
            print("""
            Invalid input.
            Please enter a letter followed by a number within the board range.
            """)
            continue
        x, y = get_coordinates(ship_input)
        if player[(x, y)] != EMPTY:
            print("""
            Starting position already occupied. Choose a different location.
            """)
            continue
        coord = (x, y)
        ship_id = id
        id_ship(player, player_ship_board, coord, ship_id)
        clear()
        draw_boards()
        while not ship_valid:
            ship_direction = input((
                'Enter your ship direction "UP, DOWN, LEFT, RIGHT"\n'
            )).upper()
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


# Places ships randomly on the board for NPC or player
def place_ships_randomly(user, ship_board, name, size, id):
    ship_valid = False
    while not ship_valid:
        x = random.randint(1, 11)
        y = random.randint(1, 11)
        ship_direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        if ship_direction == "UP":
            if (x, y-size) in user:
                if all(user[(x, y - i)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        coord = (x, y - i)
                        ship_id = id
                        id_ship(user, ship_board, coord, ship_id)
                    ship_valid = True
        elif ship_direction == "DOWN":
            if (x, y+size) in user:
                if all(user[(x, y + i)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        coord = (x, y + i)
                        ship_id = id
                        id_ship(user, ship_board, coord, ship_id)
                    ship_valid = True
        elif ship_direction == "LEFT":
            if (x-size, y) in user:
                if all(user[(x - i, y)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        coord = (x - i, y)
                        ship_id = id
                        id_ship(user, ship_board, coord, ship_id)
                    ship_valid = True
        elif ship_direction == "RIGHT":
            if (x+size, y) in user:
                if all(user[(x + i, y)] == EMPTY for i in range(1, size)):
                    for i in range(1, size):
                        coord = (x + i, y)
                        ship_id = id
                        id_ship(user, ship_board, coord, ship_id)
                    ship_valid = True
    clear()
    draw_boards()


# Displays both player and NPC boards
def draw_boards():
    print("₪₪₪₪₪₪₪₪ PLAYER'S BOARD ₪₪₪₪₪₪₪₪")
    player.draw(use_borders=False)
    print("₪₪₪₪₪₪₪ COMPUTER'S BOARD ₪₪₪₪₪₪₪")
    npc.draw(use_borders=False)


# Manages player's turn to attack
def players_turn():
    attack_valid = False
    while not attack_valid:
        ship_input = input((
            f'Your turn! Enter your the location of your attack! E.g."H5"\n'
        )).upper()
        if not is_valid_input(ship_input):
            print("""
            Invalid input.
            Please enter a letter followed by a number within the board range.
            """)
            continue
        x, y = get_coordinates(ship_input)
        if npc[(x, y)] == EMPTY:
            npc[(x, y)] = MISS
            clear()
            draw_boards()
            print("You missed!")
            attack_valid = True
        elif npc[(x, y)] == NPC_SHIP:
            npc[(x, y)] = HIT
            id = npc_ship_board[(x, y)]
            del npc_ship_board[(x, y)]
            clear()
            won = check_win(npc_ship_board)
            if not won:
                game_over("player")
            draw_boards()
            sinked = check_sunken_ship(npc_ship_board, id)
            if sinked:
                print("You hit and sunk the ship!")
            else:
                print("You hit the ship!")
            attack_valid = False
        elif npc[(x, y)] == HIT or npc[(x, y)] == MISS:
            print("""
            You already attacked that location. Try a different location.
            """)


# Checks if a ship is sunk
def check_sunken_ship(ship_board, id):
    for coord, data in ship_board.iterdata():
        if data == id:
            return False
    return True


# Manages easy NPC's turn to attack
def easy_npc_turn():
    attack_valid = False
    while not attack_valid:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        if player[(x, y)] == EMPTY:
            player[(x, y)] = MISS
            clear()
            draw_boards()
            print(f"Computer attacked {chr(x+64)}{y} and missed!")
            attack_valid = True
        elif player[(x, y)] == SHIP:
            player[(x, y)] = HIT
            del player_ship_board[(x, y)]
            ship_id = player_ship_board[(x, y)]
            sinked = check_sunken_ship(player_ship_board, ship_id)
            clear()
            draw_boards()
            if sinked:
                print(f"Computer attacked {chr(x+64)}{y} and sank your ship!")
                time.sleep(2)
            else:
                print(f"Computer attacked {chr(x+64)}{y} and hit your ship!")
                time.sleep(2)
                attack_valid = False
        else:
            # If the location has already been guessed,
            # continue the loop to find a new target.
            continue


def add_potential_targets(x, y):
    # Adds surrounding coordinates to potential targets
    # if they are within bounds and not already guessed.
    possible_targets = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for target in possible_targets:
        tx, ty = target
        if (tx, ty) in player:
            if player[target] not in [MISS, HIT] and target not in potential_targets:
                potential_targets.append(target)


# Manages hard NPC's turn to attack
def hard_npc_turn():
    global potential_targets
    attack_valid = False
    while not attack_valid:
        if potential_targets:
            # Choose the next target from potential targets
            x, y = potential_targets.pop(0)
        else:
            # Randomly select a target if no potential targets
            x = random.randint(1, 10)
            y = random.randint(1, 10)

        if player[(x, y)] == EMPTY:
            player[(x, y)] = MISS
            clear()
            draw_boards()
            print(f"Computer attacked {chr(x+64)}{y} and missed!")
            attack_valid = True
        elif player[(x, y)] == SHIP:
            player[(x, y)] = HIT
            del player_ship_board[(x, y)]
            ship_id = player_ship_board[(x, y)]
            sinked = check_sunken_ship(player_ship_board, ship_id)
            add_potential_targets(x, y)
            clear()
            draw_boards()
            if sinked:
                print(f"Computer attacked {chr(x+64)}{y} and sank your ship!")
                potential_targets = []
                time.sleep(2)
            else:
                print(f"Computer attacked {chr(x+64)}{y} and hit your ship!")
                time.sleep(2)
            attack_valid = False
        else:
            # If the location has already been guessed,
            # continue the loop to find a new target.
            continue


# Manages expert NPC's turn to attack
def expert_npc_turn():
    global potential_targets, hit_streak, attack_direction, attack_direction_reverse
    attack_valid = False
    while not attack_valid:
        if potential_targets:
            if hit_streak and attack_direction:
                # Continue along the current attack direction
                if attack_direction == "HORIZONTAL":
                    x, y = hit_streak[-1]
                    if attack_direction_reverse:
                        x -= 1
                    else:
                        x += 1
                elif attack_direction == "VERTICAL":
                    x, y = hit_streak[-1]
                    if attack_direction_reverse:
                        y -= 1
                    else:
                        y += 1
                if not ((x, y) in player) or player[(x, y)] in [MISS, HIT]:
                    attack_direction_reverse = not attack_direction_reverse
                    if attack_direction == "HORIZONTAL":
                        x, y = hit_streak[0]
                        if attack_direction_reverse:
                            x -= 1
                        else:
                            x += 1
                    elif attack_direction == "VERTICAL":
                        x, y = hit_streak[0]
                        if attack_direction_reverse:
                            y -= 1
                        else:
                            y += 1
            else:
                # Choose the next target from potential targets
                x, y = potential_targets.pop(0)
        else:
            # Randomly select a target if no potential targets
            x = random.randint(1, 10)
            y = random.randint(1, 10)
        if (x, y) in player:
            if player[(x, y)] == EMPTY:
                player[(x, y)] = MISS
                clear()
                draw_boards()
                print(f"Computer attacked {chr(x+64)}{y} and missed!")
                attack_valid = True
                if hit_streak:
                    # Reverse direction if miss after hit streak
                    attack_direction_reverse = not attack_direction_reverse
            elif player[(x, y)] == SHIP:
                player[(x, y)] = HIT
                ship_id = player_ship_board[(x, y)]
                del player_ship_board[(x, y)]
                sinked = check_sunken_ship(player_ship_board, ship_id)
                hit_streak.append((x, y))
                add_potential_targets(x, y)
                clear()
                draw_boards()
                if sinked:
                    print(f"""
                    Computer attacked {chr(x+64)}{y} and sank your ship!
                    """)
                    time.sleep(2)
                    potential_targets = []
                    hit_streak = []
                    attack_direction = None
                    attack_direction_reverse = False
                else:
                    print(f"""
                    Computer attacked {chr(x+64)}{y} and hit your ship!
                    """)
                    time.sleep(2)
                    if len(hit_streak) == 2 and not attack_direction:
                        # Determine direction based on two consecutive hits
                        if hit_streak[0][0] == hit_streak[1][0]:
                            attack_direction = "VERTICAL"
                        else:
                            attack_direction = "HORIZONTAL"
                attack_valid = False
            else:
                # If the location has already been guessed,
                # continue the loop to find a new target.
                continue


# Handle the selecetion of difficulty level
def player_difficulty(difficulty):
    difficulty()


# Checks if all ships are sunk, indicating a win
def check_win(ship_board):
    return bool(ship_board)


# Ends the game with a win message
def game_over(winner):
    if winner == "player":
        print("""
        Congratulations! You have sunk all enemy ships and won the game!
        """)
    elif winner == "npc":
        print("Game Over! The NPC has sunk all your ships.")
    sys.exit()


# Displays the main menu and handles user input
def main_menu():
    while True:
        clear()
        print("""
        ====================================
                    BATTLESHIP
        ====================================
        1. Start Game
        2. Instructions
        3. Exit
        """)
        choice = input("Enter your choice (1-3): \n").strip()
        if choice == "1":
            select_difficulty()
        elif choice == "2":
            display_instructions()
        elif choice == "3":
            clear()
            print("Exiting the game. Goodbye!")
            time.sleep(2)
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            time.sleep(2)


# Displays game instructions
def display_instructions():
    clear()
    instructions = """
    Welcome to Battleship!

    Instructions:
    1. The game is played on two grids, one for each player (you and the NPC).
    2. Each player places their ships on their grid.
    3. Ships can be placed vertically or horizontally.
    4. Each player has a fleet of ships of different lengths:
       - Carrier (5 cells)
       - Battleship (4 cells)
       - Destroyer (3 cells)
       - Submarine (3 cells)
       - Patrol Boat (2 cells)
    5. Players take turns guessing the location of the opponent's ships.
    6. If a guess hits an enemy ship, it is marked as 'X'.
    7. If a guess misses, it is marked as 'O'.
    8. If a player hits a ship, they will attack again.
    9. The first player to sink all of the opponent's ships wins.


    Press Enter to return to the main menu.
    """
    print(instructions)
    input()


# Menu select, option for difficulty level
def select_difficulty():
    while True:
        clear()
        print("""
        ====================================
                    BATTLESHIP
        ====================================
            Pick your difficulty level!
        1. EASY
        2. HARD
        3. EXPERT
        """)

        choice = input("Enter your choice (1-3): \n").strip()
        if choice == "1":
            difficulty_level = EASY
            select_placement()
        elif choice == "2":
            difficulty_level = HARD
            select_placement()
        elif choice == "3":
            difficulty_level = EXPERT
            select_placement()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            time.sleep(2)


# Menu select, Option for ship placement
def select_placement():
    while True:
        clear()
        print("""
        ====================================
                    BATTLESHIP
        ====================================
            Do you want to place your ships
                manually or randomly?

        1. Manually
        2. Randomly
        """)

        choice = input("Enter your choice (1-2): \n").strip()
        if choice == "1":
            game_start(False)
        elif choice == "2":
            game_start(True)
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            time.sleep(2)


# Controls if player place the ships manually or randomly
def player_placment(randomly):
    if randomly:
        player[0, 0] = SHIP
        place_ships_randomly(player, player_ship_board, "Carrier", 6, 5)
        place_ships_randomly(player, player_ship_board, "Battleship", 5, 4)
        place_ships_randomly(player, player_ship_board, "Destroyer", 4, 3)
        place_ships_randomly(player, player_ship_board, "Submarine", 4, 2)
        place_ships_randomly(player, player_ship_board, "Patrol Boat", 3, 1)
    else:
        player[0, 0] = SHIP
        clear()
        draw_boards()
        place_ships("Carrier", 5, 5)
        place_ships("Battleship", 4, 4)
        place_ships("Destroyer", 3, 3)
        place_ships("Submarine", 3, 2)
        place_ships("Patrol Boat", 2, 1)


# Initializes game setup
def main():
    create_board(npc)
    create_board(player)
    main_menu()


def game_start(placment_option):
    clear()
    print("Starting the game...")
    time.sleep(2)  # Pause for dramatic effect
    clear()
    place_ships_randomly(npc, npc_ship_board, "Carrier", 6, 5)
    place_ships_randomly(npc, npc_ship_board, "Battleship", 5, 4)
    place_ships_randomly(npc, npc_ship_board, "Destroyer", 4, 3)
    place_ships_randomly(npc, npc_ship_board, "Submarine", 4, 2)
    place_ships_randomly(npc, npc_ship_board, "Patrol Boat", 3, 1)
    player_placment(placment_option)
    game_play()


# Handle game play
def game_play():
    game_finished = False
    won = False
    clear()
    draw_boards()
    while not game_finished:
        players_turn()
        if won:
            game_over("player")
            game_finished = True
        print("Computer's turn!")
        player_difficulty(difficulty_level)
        if won:
            game_over("npc")
            game_finished = True


# Difficulty level varible
EASY = easy_npc_turn
HARD = hard_npc_turn
EXPERT = expert_npc_turn
difficulty_level = EASY


# Entry point for the game
main()
