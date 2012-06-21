#          Copyright Michael Kristofik 2011-2012.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          http://www.boost.org/LICENSE_1_0.txt)

"""Tic-tac-toe game where the computer player goes first."""

import ai
import rules

player_char = 'o'
comp_char = 'x'
board = [' '] * 9
winner = None
first_move = True

legend = "123456789"
rules.printBoard(legend)
print "\nComputer goes first\n"

while not winner and not rules.isFull(board):
    # On the first turn, skip the human player to let the computer go first.
    if not first_move:
        # Player's turn
        board[ai.humanPlayer(board)] = player_char
        winner = rules.getWinner(board)

    # Computer's turn
    if not winner and not rules.isFull(board):
        if first_move:
            board[ai.firstMove()] = comp_char
        else:
            # Don't care what the score was, just take the best move.
            _, move = ai.negamax(board, comp_char)
            assert move is not None
            board[move] = comp_char
        winner = rules.getWinner(board)

    # Either the game just ended or we're on to the next round.
    first_move = False
    rules.printBoard(board)

rules.printEndGame(winner)
