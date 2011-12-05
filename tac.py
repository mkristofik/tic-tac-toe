import ai
import random
import rules
import sys

player_char = 'x'
comp_char = 'o'

def playerGoesFirst():
    return len(sys.argv) <= 1 or sys.argv[1] != '2'

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
            board[ai.firstMove()] = comp_char
        else:
            # Don't care what the score was, just take the best move.
            _, move = ai.negamax(board, comp_char)
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
