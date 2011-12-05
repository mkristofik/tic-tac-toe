"""AI routines for a tic-tac-toe game."""

import copy
import random
import rules

def firstMove():
    """Return the index of a random corner.

    xkcd says the optimal first move is in a corner.

    """
    return random.choice(rules.corners)

def humanPlayer(board):
    """Get the index of square chosen by a human player."""
    while True:
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
        return c

def negamax(board, player_to_move):
    """Use a variation of the Negamax algorithm to choose the next move.

    Recursively determine the best next move for the given player.  Return a
    tuple containing the score and the board index of the move (chosen randomly
    if there are several best moves).  The score is the likely outcome of the
    game on that line of play: -1 for a loss, 0 for a draw, 1 for a win.
    Source: http://en.wikipedia.org/wiki/Negamax.

    """
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
        # Get the best response to this move.  Don't care what it was, just
        # score it.
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

def playRandomly(board):
    """Return the index of a random open square."""
    return random.choice(rules.getOpenSquares(board))

def tryToBeSmart(board, char):
    """Naive algorithm for choosing the next best move.

    Return the index of the best move we can determine from a simple set of
    rules.  Plays much better than random but is still beatable.

    """
    # If there's a move that will win you the game, take it.
    winnable = rules.chanceToWin(board, char)
    if winnable > -1:
        return winnable
    # If the player has a chance to win, block.
    block = rules.chanceToWin(board, rules.getOpposite(char))
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
