import random

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
        print("Ooops player is already in that spot!")

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
def checkRow(board):
    global winner
    if board[0] == board[7] == board[14] == board[21] and board[0] != "--":
        winner = board[0]
        return True
    elif board[7] == board[14] == board[21] == board[28] and board[7] != "--":
        winner = board[7]
        return True
    elif board[14] == board[21] == board[28] == board[35] and board[14] != "--":
        winner = board[14]
        return True
    elif board[1] == board[8] == board[15] == board[22] and board[1] != "--":
        winner = board[1]
        return True
    elif board[8] == board[15] == board[22] == board[29] and board[8] != "--":
        winner = board[8]
        return True
    elif board[15] == board[22] == board[29] == board[36] and board[15] != "--":
        winner = board[15]
        return True
    elif board[2] == board[9] == board[16] == board[23] and board[2] != "--":
        winner = board[2]
        return True
    elif board[9] == board[16] == board[23] == board[30] and board[9] != "--":
        winner = board[9]
        return True
    elif board[16] == board[23] == board[30] == board[37] and board[16] != "--":
        winner = board[16]
        return True
    elif board[3] == board[10] == board[17] == board[24] and board[3] != "--":
        winner = board[3]
        return True
    elif board[10] == board[17] == board[24] == board[31] and board[10] != "--":
        winner = board[10]
        return True
    elif board[17] == board[24] == board[31] == board[38] and board[17] != "--":
        winner = board[17]
        return True
    elif board[4] == board[11] == board[18] == board[25] and board[4] != "--":
        winner = board[4]
        return True
    elif board[11] == board[18] == board[25] == board[32] and board[11] != "--":
        winner = board[11]
        return True
    elif board[18] == board[25] == board[32] == board[39] and board[18] != "--":
        winner = board[18]
        return True
    elif board[5] == board[12] == board[19] == board[26] and board[5] != "--":
        winner = board[5]
        return True
    elif board[12] == board[19] == board[26] == board[33] and board[12] != "--":
        winner = board[12]
        return True
    elif board[19] == board[26] == board[33] == board[40] and board[19] != "--":
        winner = board[19]
        return True
    elif board[6] == board[13] == board[20] == board[27] and board[6] != "--":
        winner = board[6]
        return True
    elif board[13] == board[20] == board[27] == board[34] and board[13] != "--":
        winner = board[13]
        return True
    elif board[20] == board[27] == board[34] == board[41] and board[20] != "--":
        winner = board[20]
        return True
def checkDiagonal(baord):
    global winner
    if board[21] == board[15] == board[9] == board[3] and board[21] != "--":
        winner = board[21]
        return True
    elif board[28] == board[22] == board[16] == board[10] and board[28] != "--":
        winner = board[28]
        return True
    elif board[22] == board[16] == board[10] == board[4] and board[22] != "--":
        winner = board[22]
        return True
    elif board[35] == board[29] == board[23] == board[17] and board[35] != "--":
        winner = board[35]
        return True
    elif board[29] == board[23] == board[17] == board[11] and board[29] != "--":
        winner = board[29]
        return True
    elif board[23] == board[17] == board[11] == board[5] and board[23] != "--":
        winner = board[23]
        return True
    elif board[36] == board[30] == board[24] == board[18] and board[36] != "--":
        winner = board[36]
        return True
    elif board[30] == board[24] == board[18] == board[12] and board[30] != "--":
        winner = board[30]
        return True
    elif board[24] == board[18] == board[12] == board[6] and board[24] != "--":
        winner = board[24]
        return True
    elif board[37] == board[31] == board[25] == board[19] and board[37] != "--":
        winner = board[37]
        return True
    elif board[31] == board[25] == board[19] == board[13] and board[31] != "--":
        winner = board[31]
        return True
    elif board[38] == board[32] == board[26] == board[20] and board[38] != "--":
        winner = board[38]
        return True
    elif board[14] == board[22] == board[30] == board[38] and board[14] != "--":
        winner = board[14]
        return True
    elif board[7] == board[15] == board[23] == board[31] and board[7] != "--":
        winner = board[7]
        return True
    elif board[15] == board[23] == board[31] == board[39] and board[15] != "--":
        winner = board[15]
        return True
    elif board[0] == board[8] == board[16] == board[24] and board[0] != "--":
        winner = board[0]
        return True
    elif board[8] == board[16] == board[24] == board[32] and board[8] != "--":
        winner = board[8]
        return True
    elif board[16] == board[24] == board[32] == board[40] and board[16] != "--":
        winner = board[16]
        return True
    elif board[1] == board[9] == board[17] == board[25] and board[1] != "--":
        winner = board[1]
        return True
    elif board[9] == board[17] == board[25] == board[33] and board[9] != "--":
        winner = board[9]
        return True
    elif board[17] == board[25] == board[33] == board[41] and board[17] != "--":
        winner = board[17]
        return True
    elif board[2] == board[10] == board[18] == board[26] and board[2] != "--":
        winner = board[2]
        return True
    elif board[10] == board[18] == board[26] == board[34] and board[10] != "--":
        winner = board[10]
        return True
    elif board[3] == board[11] == board[19] == board[27] and board[3] != "--":
        winner = board[3]
        return True

def checkTie(board):
    global gameRunning
    if "--" not in board:
        printBoard(board)
        print("its a tie!")
        gameRunning = False
def checkWin():
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")

# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "o"
    else:
        currentPlayer = "x"

#computer
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 41)
        if board[position] == "--":
            board[position] = "0"
            switchPlayer()

#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)


