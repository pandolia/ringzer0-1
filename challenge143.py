# -*- coding: utf-8 -*-
import pxssh
import string

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

    trall=string.maketrans('','')
    nodigs=trall.translate(trall, string.digits)
    sudoku = False
    grille = ""

    ssh = pxssh.pxssh()
    ssh.login("ringzer0team.com", username="sudoku", password="dg43zz6R0E", port="12643", auto_prompt_reset=False, original_prompt="Solution:")
    #ssh.prompt()
    output = ssh.before

    for output_line in output.split('\r\n'):
        print output_line
        if "Solve" in output_line:
            sudoku = False
        if sudoku == True:
            grille += output_line
        if '+' in output_line:
            sudoku = True
    tosolve_withstuff = grille[82:].replace("   ","0")
    tosolve = tosolve_withstuff.translate(trall, nodigs)

    inx=0
    grille2 = [[0 for x in range(9)] for x in range(9)]

    for a in range(9):
        for b in range(9):
            grille2[a][b] = int(tosolve[inx])
            inx += 1

    print solveSudoku(grille2)

    ssh.prompt()

    reply = ""
    for a in range(9):
        for b in range(9):
            reply += str(grille2[a][b])
            reply += ","

    print reply[:-1]
    ssh.sendline("{}\r\n".format(reply[:-1]))
    #ssh.prompt()
    print(ssh.before)
