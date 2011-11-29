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


legend = "123456789"
printBoard(legend)
print "\nEnter # of square:"

first_player = True
board = [' '] * 9
s = raw_input()
while len(s) > 0:
    if not s[0].isdigit():
        continue

    c = int(s[0]) - 1
    if 0 <= c <= 8 and board[c] == ' ':
        if first_player:
            board[c] = 'x'
        else:
            board[c] = 'o'
        first_player = not first_player
        printBoard(board)  # only display a new board for a legal move

    w = getWinner(board)
    if w > 0:
        print "\nPlayer " + str(w) + " wins!"
        break

    s = raw_input()
