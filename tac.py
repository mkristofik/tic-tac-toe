import random

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
        square = board[w[0]]  # pretend all squares will be the same
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


legend = "123456789"
printBoard(legend)
print "\nEnter # of square:"

board = [' '] * 9
winner = 0
while not winner and not isFull(board):
    player_moved = False
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
        board[c] = 'x'

        # Did the player win?
        winner = getWinner(board)

    # If we get here, player moved but he didn't win, so computer gets a turn.
    if not winner and not isFull(board):
        i = random.choice(getOpenSquares(board))
        board[i] = 'o'

        # Did the computer win?
        winner = getWinner(board)

    # Either the game just ended or we're on to the next round.
    printBoard(board)

if winner:
    print "\nPlayer " + str(winner) + " wins!"
else:
    print "\nCat's game.  How boring."
