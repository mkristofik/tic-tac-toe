"""Computer-only tic-tac-toe game of a naive algorithm vs. a good one."""

import ai
import rules
import sys

naive_char = 'x'
smart_char = 'o'
naive_goes_first = True

# Pass a 2 on the command-line to let the smart algorithm go first.
if len(sys.argv) > 1 and sys.argv[1] == '2':
    naive_char, smart_char = smart_char, naive_char
    naive_goes_first = False

board = [' '] * 9
winner = None
first_move = True

while not winner and not rules.isFull(board):
    # Skip the naive player's first turn if the smart player goes first.
    if not first_move or naive_goes_first:
        # Naive player's turn.
        if first_move:
            board[ai.firstMove()] = naive_char
        else:
            board[ai.tryToBeSmart(board, naive_char)] = naive_char
        winner = rules.getWinner(board)
        first_move = False

    if not winner and not rules.isFull(board):
        # Smart player's turn
        if first_move:
            board[ai.firstMove()] = smart_char
        else:
            # Don't care what the score was, just take the best move.
            _, move = ai.negamax(board, smart_char)
            assert move is not None
            board[move] = smart_char
        winner = rules.getWinner(board)
        first_move = False

    # Either the game just ended or we're on to the next round.
    rules.printBoard(board)
    print

rules.printEndGame(winner)
