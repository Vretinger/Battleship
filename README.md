# Battleship Game

Welcome to the Battleship Game! This project is a python terminal-based implementation of the classic Battleship game where you can play against the computer. The game runs in the Code institute mock terminal on Heroku. 

The game involves strategic placement and guessing of ship locations to sink your opponent's fleet before they sink yours.

[Press me to play the live version of the game!](https://ci-battleship-8283296ac1b0.herokuapp.com/)

<img src="Images/BattleShipShowcaseImage.png" alt="Battleship game, Showcase how the game looks like when playing" width="600" height="400">


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
- **Main Menu**: Start the game, view instructions, or exit.
  
  ![An image showing the main menu with 3 different options](Images/MainMenu.png)

- **Player and Computer Boards**: Separate boards for the player and the Computer.
  
  ![An image of the game boards showing 2 separate boards. One for the computer and one for the player](Images/GameBoards.png)

- **Ship Placement**: Place ships manually or randomly.
  
  ![Showing the menu selection to pick either manual placement or random placement](Images/PlacementOption.png)

- **Turn-based Gameplay**: Players take turns guessing the location of the opponent's ships.

- **Different Difficulty Levels**: Players can choose between three different difficulties.
  
  - **Easy**: In easy mode, the computer will randomly guess the next attack location even after a hit.
  - **Hard**: In hard mode, the computer will guess random locations around the hit location until the ship is sunk.
  - **Expert**: In expert mode, the computer will determine the direction of the ship after the second hit and will then attack along that line until the ship is sunk.
  
  ![Showing the menu option for different difficulty levels](Images/DifficultyLevels.png)

- **Clear Terminal Screen**: The terminal screen is cleared to enhance the gameplay experience.

- **Accept User Input**:
  
  ![Shows a simple image of writing in a coordinate](Images/EnterInput.png)

- **Validate the Input**:
  - You cannot place ships outside the board.
  - Ships cannot overlap.
  - When attacking, coordinates cannot be outside the board.
  - You must enter coordinates in the correct format (Letter, Number).
  - You cannot guess the same location twice.
  
  ![Shows an image of different attempts of input that are either already guessed, outside the board, or just random inputs](Images/ValidateInput.png)


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

## Testing
I have manually tested this project. The testing covered the following areas:

#### **Unit Tests**
- **Board Initialization**: Verified that the game boards for both the player and computer are correctly initialized and displayed.
- **Ship Placement**: Tested manual and random ship placement to ensure ships are placed within bounds and do not overlap.
- **Coordinate Translation**: Ensured that user inputs (e.g., "H5") are correctly translated into board coordinates.
- **Ship Identification**: Confirmed that ships are correctly identified and placed on the board based on user input.
- **Attack Functionality**: Checked that attacks are correctly registered on the board, including hits, misses, and marking of sunken ships.

#### **Integration Tests**
- **Game Flow**: Ensured smooth game flow from the main menu to gameplay and end game scenarios.
- **Player Turns**: Verified that player turns correctly handle attacks and display updated boards.
- **Computer Turns**: Tested computer turns across all difficulty levels (Easy, Hard, Expert) to ensure they make valid moves and follow the intended strategy.
- **Win Conditions**: Confirmed that the game correctly identifies win conditions and displays appropriate messages.
#### **User Interface Tests**
- **Board Display**: Ensured the board is displayed correctly after each move, with accurate representation of hits, misses, and ships.
- **Menu Navigation**: Verified that all menu options (e.g., start game, select difficulty, instructions) are accessible and function as expected.
- **Instructions Display**: Checked that the instructions are clearly displayed and provide sufficient information for gameplay.


### Bug Fixing
- **Bug**: NPC Hitting Outside Board
    - **Issue**: The NPC occasionally targeted positions outside the valid board range.
    - **Solution**: Implemented checks to ensure the NPC only selects valid coordinates within the board boundaries.
- **Bug**: Expert NPC Not Attacking in Direction of Adjacent Hits
    - **Issue**: The Expert NPC did not always continue attacking in the direction of adjacent hits.
    - **Solution**: Improved the logic for the Expert NPC to remember the direction of hits and continue attacking along that line until the ship is sunk or a miss is encountered.
- **Bug**: Placing Ships Left or Right
    - **Issue**: The logic for placing ships to the left or right did not correctly account for board boundaries.
    - **Solution**: Added checks to ensure ships placed left or right do not go out of bounds and correctly occupy the intended cells.


## Deployment
This project was deployed using Code Institue's mock terminal for Heroku.
- **Steps for deployment**
    - Fork or clone this repository
    - Create a new Heroku app
    - Add a config Var in Heroku's Settings. The key is PORT and the value is 8000.
    - Set the buildpacks to "Python" and "NodeJS" in that order
    - Link the Heroku app to the repository
    - Click on **Deploy**


## Credits
- Code Institute for the deployment terminal
- [Tim Golden for the Board module pack.](https://pypi.org/project/board/#description)



