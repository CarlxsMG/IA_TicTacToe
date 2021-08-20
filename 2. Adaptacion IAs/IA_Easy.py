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
        
    return int(entradaFila), int(entradaColumna)
    
## LISTA DE CASILLAS VACIAS -- SE CREA UNA LISTA CON LISTAS DENTRO, CON LOS VALORES DISPONIBLES DE SU RESPECTIVA FILA
def MakeListOfFreeFields(board):

    current_board = []

    for i in range(3):
        current_board.append([])

        for j in range(3):
            if(j == board[i][j]):
                current_board[i].append(j)

    print(f"Los huecos disponibles de F0: {board[0]} \nLos huecos disponibles de F1: {board[1]} \nLos huecos disponibles de F2: {board[2]}")

    return current_board
    
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
        
    return int(entradaFilaIA), int(entradaColumnaIA)

## MODO DE JUEGO
def game_mode():
    import random

    arriba_izq="╔"
    abajo_izq="╚"
    arriba_der="╗"
    abajo_der="╝"
    horizontal="═"
    vertical="║"
    espacio=" "

    mode = ["_GAME_MODE_","1. USER FIRST 'O'","2. IA FIRST 'X'","3. RANDOM","0. SALIR"]
    opciones = ["1","2","3","0"]

    ancho = 40

    print(arriba_izq + horizontal*(ancho) + arriba_der)
    print(vertical + espacio*(ancho) + vertical)
    print(vertical + (mode[0]).center(int(ancho),espacio) + vertical)
    print(vertical + espacio*(ancho) + vertical)

    for i in range (1,5):
        print(vertical + horizontal*(ancho) + vertical)
        print(vertical + (mode[i]).center(int(ancho), espacio) + vertical)
        print(vertical + horizontal*(ancho) + vertical)
  
    print(abajo_izq + horizontal*(ancho) + abajo_der)

    game_mode = input("\nSELECCIONA EL MODO DE JUEGO\n")

    while game_mode not in opciones:
        game_mode = input("\nSELECCIONA EL MODO DE JUEGO\n")

    if game_mode == "3":
        game_mode = str(random.randrange(1,3))

    return game_mode

## ---------------------------------------------------------------------------------------------------------------------

board = [[i for i in range(3)] for j in range(3)]   ## CREA EL TABLERO
movement = [0,0]

turnos = 0    ## TURNOS PARTIDA
turno_IA = 0  ## TURNOS IA PARTIDA

game_on = True

game_mode_var = game_mode()

if(game_mode_var == "0"):   ## JUEGO DESACTIVADO  
    game_on = False         ## SALIR

## JUEGO ACTIVO
while game_on:

    if game_mode_var == "1" :
        DisplayBoard(board)                     ## PRINTEA EL TABLERO
        MakeListOfFreeFields(board)             ## LISTA DE POSICIONES VACIAS
        movement = EnterMove(board)             ## MOVIMIENTO USER
        board[movement[0]][movement[1]] = "O"   ## INSERTAR MOV USER

    elif game_mode_var == "2":                                            ## ACTUALIZA LOS COMBOS
        movement = DrawMove(board)                                        ## MOVIMIENTO IA
        turno_IA += 1                                                               ## MAS 1 TURNO IA
        board[movement[0]][movement[1]] = "X"                                       ## INSERTAR MOV IA

    turnos += 1     ## TURNO +1

    if VictoryFor(board)=="X" or VictoryFor(board)=="O" or turnos == 9: ## MIRA SI HAY VICTORIA O NO HAY MAS TURNOS DISPONIBLES
        break
    
    if game_mode_var == "1" :                                            ## ACTUALIZA LOS COMBOS
        movement = DrawMove(board)     ## MOVIMIENTO IA
        turno_IA += 1                                                               ## MAS 1 TURNO IA
        board[movement[0]][movement[1]] = "X"                                       ## INSERTAR MOV IA

    elif game_mode_var == "2":
        DisplayBoard(board)                     ## PRINTEA EL TABLERO
        MakeListOfFreeFields(board)             ## LISTA DE POSICIONES VACIAS
        movement = EnterMove(board)             ## MOVIMIENTO USER
        board[movement[0]][movement[1]] = "O"   ## INSERTAR MOV USER

    turnos += 1     ## TURNO +1

    if VictoryFor(board)=="X" or VictoryFor(board)=="O" or (turnos == 9):   ## MIRA SI HAY VICTORIA O NO HAY MAS TURNOS DISPONIBLES
        break


if(VictoryFor(board)=="X"):
    print("\nEl ganador es la IA, (X)\nEl user ha perdido, (O)\n")
elif(VictoryFor(board)=="O"):
    print("\nEl ganador es user, (O)\nLa IA ha perdido, (X)\n")
elif turnos == 9:
    print("\nHa sido un empate tecnico\n")

DisplayBoard(board)