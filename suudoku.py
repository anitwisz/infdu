fr = open("sudoku.txt.txt","r")

sudoku = []
for riadok in fr:
    temp = []
    riadok = riadok.strip().split(',')

    for cislo in riadok:
        temp.append(int(cislo))
    sudoku.append(temp)


def check(y,x,n):
    global sudoku
    for i in range(0,9):
        if sudoku[y][i] == n:
            return False
    for i in range(0,9):
        if sudoku[i][x] == n:
            return False
    y0 = (y//3)*3
    x0 = (x//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[y0+i][x0+i] == n:
                return False
    return True


print(check(0,6,6))