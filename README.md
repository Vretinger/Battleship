# Battleship Game

Welcome to the Battleship Game! This project is a python terminal-based implementation of the classic Battleship game where you can play against the computer. The game runs in the Code institute mock terminal on Heroku. 

The game involves strategic placement and guessing of ship locations to sink your opponent's fleet before they sink yours.

Press me to play the live version of the game!

"add images here"


## Game Instructions

- The game is played on two grids, one for each player (you and the Computer).
- Each player places their ships on their grid.
- Ships can be placed vertically or horizontally.
- Players take turns guessing the location of the opponent's ships.
- The first player to sink all of the opponent's ships wins.

## How to Play
### Main Menu:
- **Start Game:** Begin a new game.
- **Instructions:** View game instructions.
- **Exit:** Exit the game.
- **Placing Ships:**
The player places ships on their board by entering coordinates and directions, or selecting to have their ships placed randomly.
The Compouter places ships randomly.

### Gameplay:
Players take turns to attack by guessing the opponent's ship locations.
Enter coordinates (e.g., H5) to make an attack.
The board will update to show hits (X) and misses (O).
If a player hits the enemy ships they will attack again til they miss.

**Winning the Game:**
The first player to sink all the opponent's ships wins the game.

## Features

### Existing features
- **Main Menu**: Start the game, view instructions, or exit. *add image*
- **Player and Computer Boards**: Separate boards for the player and the Computer. *add image*
- **Ship Placement**: Place ships manually or randomly. *add image*
- **Turn-based Gameplay**: Players take turns guessing the location of the opponent's ships. *add image*
- **Different difficulty levels**: Player can chose between three diffrent difficulties.
    - **Easy**: In easy mode the computer will randomly guess next attack location even after hit.
    - **Hard**: In hard mode the computer will guess random location around the hit location til the ship has sunked.
    - **Expert**: In expert mode the computer will figure out in what direction the ship is after the second hit on the ship and will then attack along that line til the ship has sunked.
- **Clear Terminal Screen**: The terminal screen is cleared to enhance gameplay experience. *add image*
- **Accept user input**
- **Validate the input**
    - You cannot place ships outside the boarder
    - Ships cannot be overlapping.
    - When attacking cordinates cannot be outside the border.
    - You must enter correct cordinates in correct format. (Letter, Number)
    - You cannot guess same location twice.

### Future features
- **Local Multiplayer**: Allow two players to play on the same device.
- **Custom Ship Sizes and Types**: Allow players to customize the types and sizes of ships.
- **Different Board Sizes**: Provide options for different board sizes (e.g., 12x12, 15x15).
- **Player Statistics**: Track player statistics such as wins, losses, hit/miss ratio, etc.
- **Global Leaderboards**: Implement leaderboards to compare scores with other players globally.
- **Campaign Mode**: Create a campaign mode with different levels and challenges.
- **Timed Mode**: Introduce a timed mode where players have to make decisions within a limited time.

## Data Model
### Board Representation
The game board is represented by a 2D grid where each cell can hold different values indicating the state of that cell.

### Data Structures
- **Board Class**: This class manages the board grid and operations related to placing ships, attacks, and drawing the board.
- **ship_list**: A list containing the names and sizes of the ships used in the game.
- **ship_sizes**: A Board object representing the sizes of the ships.
- **npc and player**: Board objects representing the NPC’s and player’s game boards.
- **npc_ship_board and player_ship_board**: Board objects tracking the ships' id on the NPC’s and player’s boards to determen when a ship is sunked.

