def solveBoard(b, row, col):
    result = False

    if row==9:
        return True, b

    else:
        if col<8:
            nextRow=row
            nextCol=col+1
        else:
            nextRow=row+1
            col=0

        if b[row][col] != 0:
            result, b = solveBoard(b, nextRow, nextCol)
            return result, b

        else:
            for num in range(1, 10):
                if isValid(b, row, col, num) == True:
                    b[row][col] = num

                    result, b = solveBoard(b, nextRow, nextCol)

                    if result == True:
                        return True

            return False