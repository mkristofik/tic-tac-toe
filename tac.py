import copy
import random
import rules
import sys

player_char = 'x'
comp_char = 'o'

def playerGoesFirst():
    return len(sys.argv) <= 1 or sys.argv[1] != '2'

# AI routines

# Return the index of a random legal move.
def playRandomly(board):
    return random.choice(rules.getOpenSquares(board))

# Try to determine the best available move and return its index.
def tryToBeSmart(board):
    # If there's a move that will win you the game, take it.
    winnable = rules.chanceToWin(board, comp_char)
    if winnable > -1:
        return winnable
    # If the player has a chance to win, block.
    block = rules.chanceToWin(board, player_char)
    if block > -1:
        return block

    # I had this...
        # If there's a move that will give you a chance to win, go there.
    # ...but it actually made the computer play worse.

    # If the center square is open, go there.
    if board[4] == ' ':
        return 4
    # If a corner is open, choose one at random.
    open_corners = [c for c in rules.corners if board[c] == ' ']
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
    # Stop recursing if you just lost.  That's the worst possible outcome.
    if rules.getWinner(board) == rules.getOpposite(player_to_move):
        return (-1, None)
    # Second stop case: a cat's game, no moves left.
    if rules.isFull(board):
        return (0, None)

    # Make a pretend move in each legal square and see how it turns out.
    best_score = -1
    best_moves = []
    for s in rules.getOpenSquares(board):
        new_board = copy.deepcopy(board)
        new_board[s] = player_to_move
        # Don't care what his best response move was, just score it.
        score, _ = negamax(new_board, rules.getOpposite(player_to_move))
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
rules.printBoard(legend)

if playerGoesFirst():
    print "\nEnter # of square:"
else:
    print "\nComputer goes first\n"
    player_char, comp_char = comp_char, player_char

board = [' '] * 9
winner = None
first_move = True
while not winner and not rules.isFull(board):
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
        winner = rules.getWinner(board)

    # Computer's turn
    if not winner and not rules.isFull(board):
        # First move optimization
        if all(square == ' ' for square in board):
            # xkcd says optimal first move is in a corner
            corner = random.choice(rules.corners)
            board[corner] = comp_char
        else:
            # Don't care what the score was, just take the best move.
            _, move = negamax(board, comp_char)
            assert move is not None
            board[move] = comp_char
        winner = rules.getWinner(board)

    # Either the game just ended or we're on to the next round.
    rules.printBoard(board)

if winner:
    num = "1" if winner == 'x' else '2'
    print "\nPlayer " + num + " wins!"
else:
    print "\nCat's game.  How boring."
