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

    ssh = pxssh.pxssh()
    ssh.login("ringzer0team.com", username="sudoku", password="dg43zz6R0E", port="12643", auto_prompt_reset=False, original_prompt="Solution:")


    output = ssh.before
    sudoku = False
    grille = ""
    all=string.maketrans('','')
    nodigs=all.translate(all, string.digits)


    for patate in output.split('\r\n'):
        if "Solve" in patate:
            sudoku = False
        if sudoku == True:
            grille += patate
        if '+' in patate:
            sudoku = True
    #print "Grille: {}".format(grille)
    tosolve = grille[82:].replace("   ","0").translate(all, nodigs)
    inx=0
    grille2 = [[tosolve for i in range(9)] for j in range(9)]

    print solveSudoku(grille2)


"""
    Reply = ""
    for i in Grille:
        for j in i:
            Reply += str(j)

    print Reply
"""
