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


legend = "123456789"
printBoard(legend)

player_char = 'x'
comp_char = 'o'
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
        i = random.choice(getOpenSquares(board))
        board[i] = comp_char
        winner = getWinner(board)

    # Either the game just ended or we're on to the next round.
    printBoard(board)

if winner:
    print "\nPlayer " + str(winner) + " wins!"
else:
    print "\nCat's game.  How boring."
