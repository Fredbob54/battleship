# this is james and abigail's battleship project

#import time time.sleep(secs)
def drawBoard (board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def scrubShip(slot):
    if slot == "S":
        return " "
    else:
        return slot

def drawBoardWithoutShip(board):
    print('   |   |')
    print(' ' + scrubShip(board[0]) + ' | ' + scrubShip(board[1]) + ' | ' + scrubShip(board[2]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + scrubShip(board[3]) + ' | ' + scrubShip(board[4]) + ' | ' + scrubShip(board[5]))
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + scrubShip(board[6]) + ' | ' + scrubShip(board[7]) + ' | ' + scrubShip(board[8]))
    print('   |   |')

def choosePosition(player_n, board):
    """
    This function lets a player choose
    where on the board to place his/her two ships
    """
    drawBoard(board)
    slot_1 = int(raw_input("Slot 1 Position Number: > "))
    board[slot_1] = "X"
    print "Player %r: select your second slot number for your ship:" % player_n
    drawBoard(board)
    slot_2 = int(raw_input("Slot 2 Position Number: > "))
    while (slot_1 + 3 != slot_2 and slot_1 - 3 != slot_2 and slot_1 + 1 != slot_2 and slot_1 - 1 != slot_2):
        print "Invalid choice! Try again!"
        slot_2 = int(raw_input("Slot 2 Position Number: > "))
    board[slot_2] = "X"
    for index, each in enumerate(board):
        if(each != "X"):
            board[index] = " "
        else:
            board[index] = "S"


def checkIfHitOrMiss(guess, opponents_board):
    """
    This function will check whether a guess
    is a hit or a miss and print out the result
    """
    opponents_slot = opponents_board[guess]
    if opponents_slot == " ":
        print "Miss!"
        opponents_board[guess] = "M"
        return "miss"
    if opponents_slot == "M" or opponents_slot == "H"
        print "You've already guess this! Try again."
        return "guess again"
    if opponents_slot == "S"
        print "You've hit the ship!"
        return "S"
        opponents_board[guess] = "H"
        for each_slot in opponents_board:
            if each_slot == "S":
                print "its the opponents turn"
                return "hit"
        print "you sunk my battleship!"
        return "sunk"

def chooseAttack(opponents_board):
    """
    This function will ask the user to
    choose a slot to attack (from 0 to 8),
    then will call checkIfHitOrMiss and save it in a variable,
    # just like we do with raw input. For example:
    # answer = raw_input()
    If the the checkIfHitOrMiss result equals "already guessed",
    then this function should make the user guess
    again until (s)he gets a slot that hasn't been guessed yet.
    Once the player has successfully chosen the slot to attack,
    this function should 'return' the checkIfHitOrMiss result
    """
    #while
    answer = raw_input("choose a number between 0 through 8 to attack")
    result = checkIfHitOrMiss(guess, opponents_board)

# the game begins here:
playerOneBoard = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8"
]
playerTwoBoard = [
    "0", "1", "2",
    "3", "4", "5",
    "6", "7", "8"
]

print "Player 1 select your first slot number for your ship:"
choosePosition(1, playerOneBoard)
print "Okay player one! here's how your board looks!"
print "Player 1 select your first slot number for your ship:"
drawBoard(playerOneBoard)
choosePosition(2, playerTwoBoard)
print "Okay player two! here's how your board looks!"
drawBoard(playerTwoBoard)
game_not_won = True
player_n_turn = 1

while game_not_won == True:
    print "Player %s its your turn now!" %player_n_turn
    if player_n_turn == 1:
        drawBoardWithoutShip(playerTwoBoard)
        result = chooseAttack(playerTwoBoard)
    if player_n_turn == 2:
        drawBoardWithoutShip(playerOneBoard)
        result = chooseAttack(playerOneBoard)
    if result == "sunk":
        print "player %s won" %player_n_turn
        game_not_won = False
    else:
        if player_n_turn == 1:
            player_n_turn = 2
        else:
            player_n_turn = 1


# we need a while loop here that keeps going
# as long as game_not_won == True.
# inside this while loop, there should be a
# print statement telling the player (1 or 2)
# that it's his/her turn to choose a slot
# to attack. After printing this,
# we need to show the player their opponent's board (without the ship)
# in order for them to see where they've attacked before,
# so this while loop should use drawBoardWithoutShip()
# and pass it the opponent's board.
# Then, this while loop should call chooseAttack and save it in a variable,
# just like we do with raw input. For example:
# answer = raw_input()
# if the result of chooseAttack equals "won", then
# we should print that this player won and break out of the while loop.
# if the result of chooseAttack does NOT equal "won",
# we should change player_n_turn to make it the other player's turn.
# This means making player_n_turn = 1 if it is currently equal to 2,
# or else making it equal to 2 if it is currently equal to 1.
