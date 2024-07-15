import board

HIT = " X "
MISS = " O "
EMPTY = "   "

npc = board.Board((11, 11))
player = board.Board((11, 11))

def create_board(user):
    user.populate(" 1234567890")  # Populate the top row with numbers
    user.populate("ABCDEFGHIJ", user.iterline((1, 0), (1, 0)))  # Populate the first column with letters
    for x in range(1, 11):
        for y in range(1, 11):
            user[x, y] = EMPTY  # Fill the rest of the board with EMPTY

create_board(npc)
create_board(player)

print("₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪ COMPUTER´S BOARD ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
npc.draw()
print("\n₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪ PLAYER´S BOARD ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪")
player.draw()
