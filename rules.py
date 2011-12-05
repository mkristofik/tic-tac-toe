"""Rules and common information for a tic-tac-toe game.

The game board can be represented by any sequence with at least 9 elements.

"""

ways_to_win = [[0,1,2], [3,4,5], [6,7,8],  # across
               [0,3,6], [1,4,7], [2,5,8],  # down
               [0,4,8], [2,4,6]]           # diagonal

corners = (0, 2, 6, 8)

def chanceToWin(board, player):
    """Can a player win on his next move?

    Try to find an open square where 'player' has a move that will win the
    game.  Return the index of that square, or -1 if none found.

    """
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

def getOpenSquares(board):
    """Return a list of the currently blank squares on the board."""
    open_squares = []
    for i, s in enumerate(board):
        if s == ' ':
            open_squares.append(i)
    return open_squares

def getOpposite(player):
    """Return the other player's symbol, 'x' for 'o', 'o' for 'x'."""
    return 'x' if player == 'o' else 'o'

def getWinner(board):
    """Return 'x', 'o', or None for the winner of the given board."""
    for w in ways_to_win:
        square = board[w[0]]  # pretend all three squares will be the same
        if all(board[i] == square for i in w):
            # if they really are the same (and not blank), return who won
            if square != ' ':
                return square
    return None

def isFull(board):
    """Return True if there are no blank squares.

    A None result from getWinner() and a True result from this function
    indicates a Cat's game.

    """
    return all(s != ' ' for s in board)

def printBoard(board):
    """Print the given tic-tac-toe board."""
    print " " + board[0] + " | " + board[1] + " | " + board[2]
    print "---+---+---"
    print " " + board[3] + " | " + board[4] + " | " + board[5]
    print "---+---+---"
    print " " + board[6] + " | " + board[7] + " | " + board[8]
