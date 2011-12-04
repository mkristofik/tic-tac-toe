import random
import sys

def printBoard(board):
    print " " + board[0] + " | " + board[1] + " | " + board[2]
    print "---+---+---"
    print " " + board[3] + " | " + board[4] + " | " + board[5]
    print "---+---+---"
    print " " + board[6] + " | " + board[7] + " | " + board[8]

ways_to_win = [[0,1,2], [3,4,5], [6,7,8],  # across
               [0,3,6], [1,4,7], [2,5,8],  # down
               [0,4,8], [2,4,6]]           # diagonal

player_char = 'x'
comp_char = 'o'

def getWinner(board):
    for w in ways_to_win:
        square = board[w[0]]  # pretend all three squares will be the same
        if all(board[i] == square for i in w):
            # if they really are, see who won
            if square == 'x':
                return 1
            elif square == 'o':
                return 2
    return 0

def getOpenSquares(board):
    open_squares = []
    for i, s in enumerate(board):
        if s == ' ':
            open_squares.append(i)
    return open_squares

def isFull(board):
    return all(s != ' ' for s in board)

def playerGoesFirst():
    return len(sys.argv) <= 1 or sys.argv[1] != '2'

# AI routines

# Return the index of a random legal move.
def playRandomly(board):
    return random.choice(getOpenSquares(board))

# Try to find an open square where 'player' has a move that will win the game.
def chanceToWin(board, player):
    for w in ways_to_win:
        matches = 0
        blank_square = -1
        for square in w:
            if board[square] == player:
                matches += 1
            elif board[square] == ' ':
                blank_square = square
        if matches == 2 and blank_square != -1:
            return blank_square
    return -1

# Try to determine the best available move and return its index.
def tryToBeSmart(board):
    # If there's a move that will win you the game, take it.
    winnable = chanceToWin(board, comp_char)
    if winnable > -1:
        return winnable
    # If the player has a chance to win, block.
    block = chanceToWin(board, player_char)
    if block > -1:
        return block

    # I had this...
        # If there's a move that will give you a chance to win, go there.
    # ...but it actually made the computer play worse.

    # If the center square is open, go there.
    if board[4] == ' ':
        return 4
    # If a corner is open, choose one at random.
    corners = [0, 2, 6, 8]
    open_corners = [c for c in corners if board[c] == ' ']
    if open_corners:
        return random.choice(open_corners)
    else:
        return playRandomly(board)


legend = "123456789"
printBoard(legend)

if playerGoesFirst():
    print "\nEnter # of square:"
else:
    print "\nComputer goes first\n"
    player_char, comp_char = comp_char, player_char

board = [' '] * 9
winner = 0
first_move = True
while not winner and not isFull(board):
    player_moved = False

    # If human player is O's, skip first turn to let computer go first.
    if first_move and player_char == 'o':
        player_moved = True
    first_move = False

    # Player's turn
    while not player_moved:
        s = raw_input()
        if len(s) == 0:
            continue
        if not s[0].isdigit():
            continue

        c = int(s[0]) - 1
        if c < 0 or c > 8:
            continue
        if board[c] != ' ':
            continue

        # We've gotten past all illegal inputs and invalid moves.
        player_moved = True
        board[c] = player_char
        winner = getWinner(board)

    # Computer's turn
    if not winner and not isFull(board):
        i = tryToBeSmart(board)
        board[i] = comp_char
        winner = getWinner(board)

    # Either the game just ended or we're on to the next round.
    printBoard(board)

if winner:
    print "\nPlayer " + str(winner) + " wins!"
else:
    print "\nCat's game.  How boring."
