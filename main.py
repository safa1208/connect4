board = ["--", "--", "--", "--", "--", "--", "--",
         "--", "--", "--", "--", "--", "--", "--",
         "--", "--", "--", "--", "--", "--", "--",
         "--", "--", "--", "--", "--", "--", "--",
         "--", "--", "--", "--", "--", "--", "--",
         "--", "--", "--", "--", "--", "--", "--"]
currentPlayer = "x"
winner = None
gameRunning = True


def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2] + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9] + "|" + board[10] + "|" + board[11] + "|" + board[12] + "|" + board[13])
    print(board[14] + "|" + board[15] + "|" + board[16] + "|" + board[17] + "|" + board[18] + "|" + board[19] + "|" + board[20])
    print(board[21] + "|" + board[22] + "|" + board[23] + "|" + board[24] + "|" + board[25] + "|" + board[26] + "|" + board[27])
    print(board[28] + "|" + board[29] + "|" + board[30] + "|" + board[31] + "|" + board[32] + "|" + board[33] + "|" + board[34])
    print(board[35] + "|" + board[36] + "|" + board[37] + "|" + board[38] + "|" + board[39] + "|" + board[40] + "|" + board[41])
printBoard(board)

def playerInput(board):
    inp = int(input("enter a number 1-42"))
    if inp>=1 and inp<=42 and board[inp-1] == "--":
        board[inp-1] = currentPlayer
    else:
        print("Ooops mplayer is already in that spot!")

#check for win (horizontle)
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] == board[3] == board[4] == board[5] == board[6] and board[1] != "--":
        winner = board [0]
        return True
    elif board[7] == board[8] == board[9] == board[10] == board[11] == board[12] == board[13] and board[8] != "--":
        winner = board[7]
        return True
    elif board[14] == board[15] == board[16] == board[17] == board[18] == board[19] == board[20] and board[15]!= "--":
        winner = board[14]
        return True
    elif board[21] == board[22] == board[23] == board[24] == board[25] == board[26] == board[27] and board[22]!= "--":
        winner = board[21]
        return True
    elif board[28] == board[29] == board[30] == board[31] == board[32] == board[33] == board[34] and board[29]!= "--":
        winner = board[28]
        return True
    elif board[35] == board[36] == board[37] == board[38] == board[39] == board[40] == board[41] and board[36]!= "--":
        winner = board[35]
        return True

#chech winner(row)
