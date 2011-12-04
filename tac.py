import copy
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
            # if they really are, return who won
            if square != ' ':
                return square
    return None

def getOpenSquares(board):
    open_squares = []
    for i, s in enumerate(board):
        if s == ' ':
            open_squares.append(i)
    return open_squares

def isFull(board):
    return all(s != ' ' for s in board)

def getOpposite(player):
    return 'x' if player == 'o' else 'o'

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

# Recursively determine the best next move for the given player.  Return the
# score and the board index of the move (chosen randomly if there are several
# best moves).  The score is the likely outcome of the game on that line of
# play: -1 for a loss, 0 for a draw, 1 for a win.
# Source: http://en.wikipedia.org/wiki/Negamax.
def negamax(board, player_to_move):
    # You just lost.  That's the worst possible outcome.
    if getWinner(board) == getOpposite(player_to_move):
        return (-1, None)
    # Cat's game, no move possible.
    if isFull(board):
        return (0, None)

    # Make a pretend move in each legal square and see how it turns out.
    best_score = -1
    best_moves = []
    for s in getOpenSquares(board):
        new_board = copy.deepcopy(board)
        new_board[s] = player_to_move
        # Don't care what his best response move was, just score it.
        score, _ = negamax(new_board, getOpposite(player_to_move))
        # The score for you is the opposite of the score for the other player.
        score *= -1
        if score == 1:
            # That move led to a win, so return it
            return (1, s)
        elif score > best_score:
            best_score = score
            best_moves = [s]
        elif score == best_score:
            best_moves.append(s)
    assert best_moves
    return (best_score, random.choice(best_moves))


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
        # First move optimization
        if all(square == ' ' for square in board):
            # xkcd says optimal first move is in a corner
            corner = random.choice((0, 2, 6, 8))
            board[corner] = comp_char
        else:
            # Don't care what the score was, just take the best move.
            _, move = negamax(board, comp_char)
            assert move is not None
            board[move] = comp_char
        winner = getWinner(board)

    # Either the game just ended or we're on to the next round.
    printBoard(board)

if winner:
    num = "1" if winner == 'x' else '2'
    print "\nPlayer " + num + " wins!"
else:
    print "\nCat's game.  How boring."
