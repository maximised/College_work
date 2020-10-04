def createBoard(n):
    b = []
    for rowNumber in range(n):
        columns = [0] * n
        '''columns = []
        for colNumber in range (n):
            columns.append(0)'''
        b.append(columns)

    return b


def isValidMove(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveBoard(b, col):
    size = len(b)

    if (col == size ):
        return b, True

    for row in range(size):
        if isValidMove(b, row, col):
            b[row][col] = 1

            if (solveBoard(b, col + 1)[0] != False):
                return b, True

            b[row][col] = 0

    return False, b







# see pseudocode above.


def printBoard(SBoard):
    for row in SBoard:
        for col in row:
            print(col, end=" ")
        print("\n")


# Main Program
n = int(input("What is the width of the board?"))

board = createBoard(n)
solvedBoard, result = solveBoard(board, 0)  # pass in the empty board (matrix) and the column to start at i.e. the first column with index 0

if result == False:
    print("Solution does not exist")
else:
    printBoard(solvedBoard)
# printBoard (board)