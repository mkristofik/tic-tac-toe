"""Tic-tac-toe game where the human player goes first."""

import ai
import rules

player_char = 'x'
comp_char = 'o'
board = [' '] * 9
winner = None

legend = "123456789"
rules.printBoard(legend)
print "\nEnter # of square:"

while not winner and not rules.isFull(board):
    # Player's turn
    board[ai.humanPlayer(board)] = player_char
    winner = rules.getWinner(board)

    # Computer's turn
    if not winner and not rules.isFull(board):
        # Don't care what the score was, just take the best move.
        _, move = ai.negamax(board, comp_char)
        assert move is not None
        board[move] = comp_char
        winner = rules.getWinner(board)

    # Either the game just ended or we're on to the next round.
    rules.printBoard(board)

rules.printEndGame(winner)
