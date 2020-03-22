n = int(input())

max = 0
for i in range(1, n+1):
    max+=i

nums = [i for i in range(1, max+1)]

triangle = [[-1]*i for i in range(n, 0, -1)]




def isValidMove(triangle, num, r, c):
    c = 0

    for row in triangle:
        c += row.count(num)

    if c > 1:
        return False

    if r == 0:
        return True


    print(r-1, c, c+1)
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