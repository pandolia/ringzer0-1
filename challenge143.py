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

    s = pxssh.pxssh()
    s.login("ringzer0team.com", "sudoku", password="dg43zz6R0E", port="12643", original_prompt="Solution:", auto_prompt_reset=False)

    sudoku = False
    grille = ""
    output =  s.before

    for i in output.split('\n'):
        if "Solve" in i:
            sudoku = False
        if sudoku == True:
            grille += str(i)
            #print grille
        if '+' in i:
            sudoku = True
    print "Grille: {}".format(grille)

"""
    Reply = ""
    for i in Grille:
        for j in i:
            Reply += str(j)

    print Reply
"""
