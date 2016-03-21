import pxssh

def findNextCellToFill(grid, i, j):
    for x in range(i,9):
        for y in range(j,9):
            if grid[x][y] == 0:
                return x,y
            for x in range(0,9):
                for y in range(0,9):
                    if grid[x][y] == 0:
                        return x,y
            return -1,-1

def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 *(i/3), 3 *(j/3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
                    return True
        return False

def solveSudoku(grid, i=0, j=0):
    i,j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):
            grid[i][j] = e
            if solveSudoku(grid, i, j):
                return True
            # Undo the current cell for backtracking
            grid[i][j] = 0
    return False


if __name__ == '__main__':

    #s = pxssh.pxssh()
    #s.login ("ringzer0team.com", "sudoku", "dg43zz6R0E", port="12643")
    #print s.before

    Grill = [[8,0,0,9,5,0,0,4,6],[0,5,0,0,0,0,0,1,3],[7,0,6,8,0,0,0,0,0],[1,0,0,0,2,0,4,0,8],[5,0,7,4,0,0,1,0,0],[0,0,8,1,3,9,0,0,0],[3,9,0,2,0,0,6,0,1],[2,7,4,6,8,1,0,0,5],[0,8,0,0,9,0,2,7,0]]
    print solveSudoku(Grill)
    Reply = ""
    for i in Grill:
        for j in i:
            Reply += str(j)

    print Reply
