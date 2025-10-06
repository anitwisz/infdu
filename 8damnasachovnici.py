
from PIL import Image

size = 5


sachovnica = []
for i in range(size):
    temp = []
    for j in range(size):
        temp.append(0)
    sachovnica.append(temp)

def check(x,y):
    for i in range(size):
        if sachovnica[y][i] == 1 or sachovnica[i][x] == 1:
            return False
    for i in range(size):
        for j in range(size):
            if i + j == x+y:
                if sachovnica[i][j] == 1:
                    return False
            if i - j == y - x:
                if sachovnica[i][j] == 1:
                    return False
    return True

def create_chessboard():
   global sachovnica
   obr = Image.new('RGB', (size,size), (255, 255, 255))
   pixels= obr.load()
   for i in range(size):
       for j in range(size):
           if (i + j) % 2:
               pixels[i, j] = (0, 0, 0)

       #for x in sachovnica:
            #for y in x:
                #if y == 1:
                     #pixels[y,y] = (255, 0, 0)

               obr.save('sach.png')




def drticka(n):
    global sachovnica
    if n == size:
        print(sachovnica)
        print('_________________')
        create_chessboard()


    else:
        for x in range(size):
            if check(x,n):
                sachovnica[n][x] = 1
                drticka(n+1)
                sachovnica[n][x] = 0

drticka(0)