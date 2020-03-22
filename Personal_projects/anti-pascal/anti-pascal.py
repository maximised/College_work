n = int(input('number of rows: '))

max = 0
for i in range(1, n+1):
    max+=i

nums = [i for i in range(1, max+1)]

triangle = [[-1]*i for i in range(n, 0, -1)]

#top is for making triangle and listing nums that are going in it later
#putting it in a function is better I know


def isValidMove(triangle, num, r, c):
    count = 0

    for row in triangle:
        count += row.count(num)

    if count > 0:
        return False

    if r == 0:
        return True

    if abs(triangle[r-1][c]-triangle[r-1][c+1]) == num:
        return True

    else:
        return False


def solveTriangle(triangle, r, c):
    if c >= (n-r):
        c = 0
        r += 1

    if r >= n:
        return True, triangle

    if triangle[r][c]!=-1:
        return solveTriangle(triangle, r, c+1)
    else:
        for num in nums:
            if isValidMove(triangle, num, r, c):
                triangle[r][c] = num
                if solveTriangle(triangle, r, c+1) != False:
                    return True, triangle

        triangle[r][c] = -1

    return False


print(solveTriangle(triangle, 0, 0))