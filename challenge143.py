import paramiko
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

#def ssh_connect():


if __name__ == '__main__':
    buff = ""
    trall=string.maketrans('','')
    nodigs=trall.translate(trall, string.digits)
    sudoku = False
    grille = ""

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("ringzer0team.com", username="sudoku", password="dg43zz6R0E", port=12643)
    ssh_term = ssh.invoke_shell()

    buff = ''
    while not buff.endswith(':'):
        resp = ssh_term.recv(9999)
        buff += resp
        #print(resp)

    for output_line in buff:
        #print output_line
        if "Solve" in output_line:
            sudoku = False
        if sudoku == True:
            grille += output_line
        if '+' in output_line:
            sudoku = True
    tosolve_withstuff = grille[82:].replace("   ","0")
    tosolve = tosolve_withstuff.translate(trall, nodigs)
    #print tosolve

    inx=0
    grille2 = [[0 for x in range(9)] for x in range(9)]

    for a in range(9):
        for b in range(9):
            grille2[a][b] = int(tosolve[inx])
            inx += 1

    print solveSudoku(grille2)
    #print grille2

    reply = ""
    for a in range(9):
        for b in range(9):
            reply += str(grille2[a][b])
            reply += ","

    print reply[:-1]
    buff = ''
    ssh_term.send(reply[:-1] + '\r\n')
    while not buff.endswith('FLAG'):
        resp = ssh_term.recv(9999)
        buff += resp
        print(resp)
