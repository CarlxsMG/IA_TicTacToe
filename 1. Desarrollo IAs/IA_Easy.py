## MAPA
def DisplayBoard(board):

    linea_h = "\t"+(("+"+"-"*7)*3)+"+"
    linea_v = "\t"+(("|"+" "*7)*3)+"|"

    ## FILA 1
    print(linea_h)
    print(linea_v)
            
    print("\t|"," ",board[0][0]," "*2,end="")
    print("|"," ",board[0][1]," "*2,end="")
    print("|"," ",board[0][2]," "*2,end="|  <------ FILA 0\n")
            
    print(linea_v)
                
    ## FILA 2
    print(linea_h)
    print(linea_v)
            
    print("\t|"," ",board[1][0]," "*2,end="")
    print("|"," ",board[1][1]," "*2,end="")
    print("|"," ",board[1][2]," "*2,end="|  <------ FILA 1\n")
            
    print(linea_v)
   
    ## FILA 3
    print(linea_h)
    print(linea_v)
    
    print("\t|"," ",board[2][0]," "*2,end="")
    print("|"," ",board[2][1]," "*2,end="")
    print("|"," ",board[2][2]," "*2,end="|  <------ FILA 2\n")
        
    print(linea_v)
    print(linea_h)
        
## ENTRADA USUARIO -- ENTRADA DE FILA Y COLUMNA
def EnterMove(board):
  
    entradaFila = input("Introduzca la fila a cambiar")
    entradaColumna = input("Introduzca la columna a cambiar")
    opciones = "012"    
    
    
    while (len(entradaFila and entradaColumna) != 1 or (int(entradaColumna) != board[int(entradaFila)][int(entradaColumna)]) or (entradaFila and entradaColumna) not in opciones) :
        entradaFila = input("Introduzca la fila a cambiar")
        entradaColumna = input("Introduzca la columna a cambiar")
        
    board[int(entradaFila)][int(entradaColumna)] = "O"
    
## LISTA DE CASILLAS VACIAS -- SE CREA UNA LISTA CON LISTAS DENTRO, CON LOS VALORES DISPONIBLES DE SU RESPECTIVA FILA
def MakeListOfFreeFields(board):

    filas = []
    columnas = []

    for i in range(3):
        for j in range(3):
            if(j == board[i][j]):
                columnas.append(j)
        filas.append(columnas)

    print(f"Los huecos disponibles de F0: {board[0]} \nLos huecos disponibles de F1: {board[1]} \nLos huecos disponibles de F2: {board[2]}")

    
## CONFIRMA EL GANADOR -- CHECKEA SI HAY ALGUN 3 EN RAYA -- DEVUELVE X/O, DEPENDE QUIEN HAYA HECHO EL COMBO
def VictoryFor(board):

    fila1 = board[0][0] == board[0][1] == board[0][2] and (board[0][0] and board[0][1] and board[0][2]) != int
    fila2 = board[1][0] == board[1][1] == board[1][2] and (board[1][0] and board[1][1] and board[1][2]) != int
    fila3 = board[2][0] == board[2][1] == board[2][2] and (board[2][0] and board[2][1] and board[2][2]) != int

    columna1 = board[0][0] == board[1][0] == board[2][0] and (board[0][0] and board[1][0] and board[2][0]) != int
    columna2 = board[0][1] == board[1][1] == board[2][1] and (board[0][1] and board[1][1] and board[2][1]) != int
    columna3 = board[0][2] == board[1][2] == board[2][2] and (board[0][2] and board[1][2] and board[2][2]) != int

    diagonal1 = board[0][0] == board[1][1] == board[2][2] and (board[0][0] and board[1][1] and board[2][2]) != int
    diagonal2 = board[0][2] == board[1][1] == board[2][0] and (board[0][2] and board[1][1] and board[0][2]) != int


    if(fila1==True):
        winner = board[0][0]
    elif(fila2==True):
        winner = board[1][0]
    elif(fila3==True):
        winner = board[2][0]
    elif(columna1==True):
        winner = board[0][0]
    elif(columna2==True):
        winner = board[0][1]
    elif(columna3==True):
        winner = board[0][2]
    elif(diagonal1==True):
        winner = board[0][0]
    elif(diagonal2==True):
        winner = board[0][2]
    else:
        winner = 0

    return winner

## MOVIMIENTO IA
def DrawMove(board):   
    import random

    entradaFilaIA = random.randrange(3)
    entradaColumnaIA = random.randrange(3)
        
    while int(entradaColumnaIA) != board[int(entradaFilaIA)][int(entradaColumnaIA)]:
        entradaFilaIA = random.randrange(3)
        entradaColumnaIA = random.randrange(3)
        
    board[int(entradaFilaIA)][int(entradaColumnaIA)] = "X"

board = [[i for i in range(3)] for j in range(3)]

turnos = 9

while True:

    DisplayBoard(board)
    MakeListOfFreeFields(board)
    EnterMove(board)
    turnos -= 1

    if(VictoryFor(board)=="X" or VictoryFor(board)=="O" or (turnos == 0)):
        break

    DrawMove(board)
    turnos -= 1

    print(VictoryFor(board))
    if(VictoryFor(board)=="X" or VictoryFor(board)=="O" or (turnos == 0)):
        break


if(VictoryFor(board)=="X"):
    print("\nEl ganador es la IA, (X)\nEl user ha perdido, (O)\n")
elif(VictoryFor(board)=="O"):
    print("\nEl ganador es user, (O)\nLa IA ha perdido, (X)\n")
elif turnos == 0:
    print("\nHa sido un empate tecnico\n")

DisplayBoard(board)