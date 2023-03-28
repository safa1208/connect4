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
    if board[0] == board[1] == board[2] == board[3] and board[0] != "--":
        winner = board [0]
        return True
    elif board[1] == board[2] == board[3] == board[4] and board[1] != "--":
        winner = board [1]
        return True
    elif board[2] == board[3] == board[4] == board[5] and board[2] != "--":
        winner = board[2]
        return True
    elif board[3] == board[4] == board[5] == board[6] and board[3] != "--":
        winner = board[3]
        return True
    elif board[7] == board[8] == board[9] == board[10] and board[7] != "--":
        winner = board[7]
        return True
    elif board[8] == board[9] == board[10] == board[11] and board[8] != "--":
        winner = board[8]
        return True
    elif board[9] == board[10] == board[11] == board[12] and board[9] != "--":
        winner = board[9]
        return True
    elif board[10] == board[11] == board[12] == board[13] and board[10] != "--":
        winner = board[10]
        return True
    elif board[14] == board[15] == board[16] == board[17] and board[14] != "--":
        winner = board[14]
        return True
    elif board[15] == board[16] == board[17] == board[18] and board[15] != "--":
        winner = board[15]
        return True
    elif board[16] == board[17] == board[18] == board[19] and board[16] != "--":
        winner = board[16]
        return True
    elif board[17] == board[18] == board[19] == board[20] and board[17] != "--":
        winner = board[17]
        return True
    elif board[21] == board[22] == board[23] == board[24] and board[21] != "--":
        winner = board[21]
        return True
    elif board[22] == board[23] == board[24] == board[25] and board[22] != "--":
        winner = board[22]
        return True
    elif board[23] == board[24] == board[25] == board[26] and board[23] != "--":
        winner = board[23]
        return True
    elif board[24] == board[25] == board[26] == board[27] and board[24] != "--":
        winner = board[24]
        return True
    elif board[28] == board[29] == board[30] == board[31] and board[28] != "--":
        winner = board[28]
        return True
    elif board[29] == board[30] == board[31] == board[32] and board[29] != "--":
        winner = board[29]
        return True
    elif board[30] == board[31] == board[32] == board[33] and board[34] != "--":
        winner = board[30]
        return True
    elif board[35] == board[36] == board[37] == board[38] and board[35] != "--":
        winner = board[35]
        return True
    elif board[36] == board[37] == board[38] == board[39] and board[36] != "--":
        winner = board[36]
        return True
    elif board[37] == board[38] == board[39] == board[40] and board[37] != "--":
        winner = board[37]
        return True
    elif board[38] == board[39] == board[40] == board[41] and board[38] != "--":
        winner = board[38]
        return True
#chech winner(row)
