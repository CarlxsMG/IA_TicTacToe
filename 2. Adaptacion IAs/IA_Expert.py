## Establecer prioridad de eleccion Sobre cerrar X o O

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
    opciones = ["0","1","2"]    
    
    
    while ((entradaFila and entradaColumna) not in opciones) or ((len(entradaFila and entradaColumna)!=1 ) or (str(board[int(entradaFila)][int(entradaColumna)]).isdigit())==False) :
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

    print(f"Los huecos disponibles de F0: {current_board[0]} \nLos huecos disponibles de F1: {current_board[1]} \nLos huecos disponibles de F2: {current_board[2]}")

    return current_board

## CONFIRMA EL GANADOR -- CHECKEA SI HAY ALGUN 3 EN RAYA -- DEVUELVE X/O, DEPENDE QUIEN HAYA HECHO EL COMBO
def VictoryFor(board):

    fila1 = board[0][0] == board[0][1] == board[0][2]
    fila2 = board[1][0] == board[1][1] == board[1][2]
    fila3 = board[2][0] == board[2][1] == board[2][2]

    columna1 = board[0][0] == board[1][0] == board[2][0] != 0
    columna2 = board[0][1] == board[1][1] == board[2][1] != 1
    columna3 = board[0][2] == board[1][2] == board[2][2] != 2

    diagonal1 = board[0][0] == board[1][1] == board[2][2]
    diagonal2 = board[0][2] == board[1][1] == board[2][0]


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
## CHECKEA LAS LINEAS DE COMBO OCUPADAS DEL TABLERO -- RECORRE EL MAPA Y GUARDA EL COMBO OCUPADO -- EVITA FALLOS DE POSICION FICHA IA Y DE FALSAS VICTORIAS
def combos_check(board,combo_check):
    combo_true=False

    ## BUSQUEDA POR FILAS
    for i in range(3):
        count = 0
        combo = []

        for j in range(3):
            combo.append([i,j])  ## CREA EL COMBO

            if(board[i][j]=="X")or(board[i][j]=="O"):
                count +=1

        if(count==3):
            combo_true=False

            for i in range(len(combo_check)):
                if(combo_check[i] == combo):
                    combo_true = True
            
            if(combo_true == False):
                combo_check+=[combo]    ## SI EL COMBO, NO ESTA EN LA LISTA DE COMBOS OCUPADOS, SE AÑADE

    ## BUSQUEDA POR COLUMNAS
    for k in range(3):
        count_x= 0
        count_o = 0
        combo=[]

        for l in range(3):
            combo.append([l,k])     ## CREA EL COMBO

            if(board[l][k]=="X"):
                count_x +=1
            elif(board[l][k]=="O"):
                count_o +=1

        if(count_x+count_o==3):
            combo_true=False

            for i in range(len(combo_check)):
                if(combo_check[i] == combo):
                    combo_true = True
            
            if(combo_true == False):
                combo_check+=[combo]    ## SI EL COMBO, NO ESTA EN LA LISTA DE COMBOS OCUPADOS, SE AÑADE

    ## BUSQUEDA POR DIAGONAL
    if(board[1][1]=="O")or(board[1][1]=="X"):
        combo_true=False

        for f in range(0,3,2):
            for q in range(0,3,2):
                if(board[f][q]=="O")or(board[f][q]=="X"):
                    combo=[]
                    combo_inv=[]

                    if(f==0):
                        f_inv=2
                    else:
                        f_inv=0
                    if(q==0):
                        q_inv=2
                    else:
                        q_inv=0

                    if(board[f_inv][q_inv])=="X" or (board[f_inv][q_inv])=="O": ## COMPRUEBA QUE EN LAS ESQUINAS ENFRENTADAS TENGAN EL MISMO VALOR (X/O)
                        combo+=[f_inv,q_inv],[1,1],[f,q]        ## CREA EL COMBO
                        combo_inv+=[f,q],[1,1],[f_inv,q_inv]    ## CREA EL COMBO
                        combo_true=False

                        for i in range(len(combo_check)):
                            if(combo_check[i] == combo)or(combo_check[i] == combo_inv):
                                combo_true = True
                            
                        if(combo_true == False):    ## SI EL COMBO, NO ESTA EN LA LISTA DE COMBOS OCUPADOS, SE AÑADE
                            combo_check+=[combo]
                            combo_check+=[combo_inv]
                    
            if(board[f][q]=="O")or(board[f][q]=="X"):   ## LO MISMO QUE EL ANTERIOR IF, PARA EL SEGUNDO BUCLE FOR
                    combo=[]
                    combo_inv = []

                    if(f==0):
                        f_inv=2
                    else:
                        f_inv=0
                    if(q==0):
                        q_inv=2
                    else:
                        q_inv=0

                    if(board[f_inv][q_inv])=="X" or (board[f_inv][q_inv])=="O": ## COMPRUEBA QUE EN LAS ESQUINAS ENFRENTADAS TENGAN EL MISMO VALOR (X/O)
                        combo+=[f_inv,q_inv],[1,1],[f,q]        ## CREA EL COMBO
                        combo_inv+=[f,q],[1,1],[f_inv,q_inv]    ## CREA EL COMBO
                        combo_true=False

                        for i in range(len(combo_check)):
                            if(combo_check[i] == combo)or(combo_check[i] == combo_inv):
                                combo_true = True
                            
                        if(combo_true == False):    ## SI EL COMBO, NO ESTA EN LA LISTA DE COMBOS OCUPADOS, SE AÑADE
                            combo_check+=[combo]
                            combo_check+=[combo_inv]
    
## BUSCA LOS COMBOS DISPONIBLES DEL TABLERO Y DEVUELVE SI HAY WIN CONDITTION, LA POSICION PARA EJECUTAR LA JUGADA, Y EL PROPIETARIO DEL COMBO (X/O)
def win_condittion(board,combo_check):
    win = False
    FilaIA = 0
    ColumnaIA = 0

    lista_variantes = [["","","",""]]

    ## BUSQUEDA POR FILAS
    for i in range(len(board)):
        if(board[i].count("X") == 2)or(board[i].count("O")== 2):
            combo=[]
            FilaIA = i

            for n in range(3):
                combo.append([i,n])     ## SE CREA EL COMBO

                if(board[i][n]!="O")and(board[i][n]!="X"):      ## BUSCA LA POSICION DISPONIBLE
                    ColumnaIA = n
                    win = True                                  ## WIN CONDITTION DISPONIBLE
                    lista_variantes.append([win,FilaIA,ColumnaIA,board[i][n-1]])    ## INSERTA EL COMBO EN LAS JUGADAS DISPONIBLES EN ESE MOMENTO DEL TABLERO

    ## BUSQUEDA POR COLUMNAS
    for j in range(3):
        count_x= 0
        count_o = 0

        for k in range(3):
            if(board[k][j]=="X"):
                count_x +=1
            elif(board[k][j]=="O"):
                count_o +=1
                
        if(count_x==2)or(count_o==2):
            combo=[]
            for h in range(3):
                combo.append([h,j]) ## SE CREA EL COMBO
                if(str(board[h][j]).isdigit()==True):   ## BUSCA LA POSICION DISPONIBLE
                    FilaIA = h
                    ColumnaIA = j
                    win = True                          ## WIN CONDITTION DISPONIBLE
                    lista_variantes.append([win,FilaIA,ColumnaIA,board[h-1][j]])    ## INSERTA EL COMBO EN LAS JUGADAS DISPONIBLES EN ESE MOMENTO DEL TABLERO

    ## BUSQUEDA POR DIAGONAL
    if(board[1][1]=="O")or(board[1][1]=="X"):   ## SI HAY VALOR CENTRAL
        for f in range(0,3,2):
            for c in range(0,3,2):
                if(board[f][c]=="O")or(board[1][1]=="X"):
                    if(f==0):
                        f_inv=2
                    else:
                        f_inv=0
                    if(c==0):
                        c_inv=2
                    else:
                        c_inv=0

                    if str(board[f_inv][c_inv]).isdigit()==True:    ## BUSCA LA POSICION DISPONIBLE
                        FilaIA=f_inv
                        ColumnaIA=c_inv
                        win = True                                  ## WIN CONDITTION DISPONIBLE
                        lista_variantes.append([win,FilaIA,ColumnaIA,board[f][c]])  ## INSERTA EL COMBO EN LAS JUGADAS DISPONIBLES EN ESE MOMENTO DEL TABLERO
                    
                    
            if(board[f][c]=="O")or(board[1][1]=="X"):   ## LO MISMO QUE EL ANTERIOR IF, PARA EL SEGUNDO BUCLE FOR
                    if(f==0):
                        f_inv=2
                    else:
                        f_inv=0
                    if(c==0):
                        c_inv=2
                    else:
                        c_inv=0

                    if str(board[f_inv][c_inv]).isdigit()==True:    ## BUSCA LA POSICION DISPONIBLE
                        FilaIA=f_inv
                        ColumnaIA=c_inv
                        win = True                                  ## WIN CONDITTION DISPONIBLE
                        lista_variantes.append([win,FilaIA,ColumnaIA,board[f][c]])      ## INSERTA EL COMBO EN LAS JUGADAS DISPONIBLES EN ESE MOMENTO DEL TABLERO

    else:   ## SI NO HAY VALOR CENTRAL
        for b in range(0,3,2):  ## BUSCA POR ESQUINAS PARA VALOR X
            if(board[0][b]=="X"):
                if b==0:
                    b_inv = 2
                else:
                    b_inv = 0

                if(board[2][b_inv]=="X"):   ## CONFIRMA SI LA ESQUINA ENFRENTADA TIENE EL MISMO VALOR
                    FilaIA = 1
                    ColumnaIA = 1
                    win = True              ## WIN CONDITTION DISPONIBLE
                    lista_variantes.append([win,FilaIA,ColumnaIA,board[2][b_inv]])  ## INSERTA EL COMBO EN LAS JUGADAS DISPONIBLES EN ESE MOMENTO DEL TABLERO
            
            if(board[0][b]=="O"):   ## BUSCA POR ESQUINAS PARA VALOR O
                if b==0:
                    b_inv = 2
                else:
                    b_inv = 0

                if(board[2][b_inv]=="O"):   ## CONFIRMA SI LA ESQUINA ENFRENTADA TIENE EL MISMO VALOR
                    FilaIA = 1
                    ColumnaIA = 1
                    win = True              ## WIN CONDITTION DISPONIBLE
                    lista_variantes.append([win,FilaIA,ColumnaIA,board[2][b_inv]])  ## INSERTA EL COMBO EN LAS JUGADAS DISPONIBLES EN ESE MOMENTO DEL TABLERO

    if(len(lista_variantes)>1): ## LA IA OBTIENE ELECCION DE RESPUESTA, CUANDO HAYA MAS DE 1 JUGADA DISPONIBLE
        for i in range(len(lista_variantes)):   ## RECORRE LAS JUGADAS DISPONIBLES

            if(lista_variantes[i][3]=="X"):     ## LAS JUGADAS DE LA IA OBTIENEN MAS IMPORTANCIA, QUE LOS CIERRES DEL CONTRINCARIO
                FilaIA=lista_variantes[i][1]
                ColumnaIA=lista_variantes[i][2]
            else:
                FilaIA=lista_variantes[1][1]
                ColumnaIA=lista_variantes[1][2]

    return win,FilaIA,ColumnaIA               

## MOVIMIENTO IA
def DrawMove(board,turno_IA,fila_mvm_IA,col_mvm_IA,combo_check):
    import random

    if(turno_IA==0):  ## PRIMER MOVIMIENTO DE LA IA ALEATORIO
        entradaFilaIA = random.randrange(0,3,2)
        entradaColumnaIA = random.randrange(0,3,2)

        while (str(board[entradaFilaIA][entradaColumnaIA]).isdigit()==False):
                entradaFilaIA = random.randrange(0,3,2)
                entradaColumnaIA = random.randrange(0,3,2)

        return entradaFilaIA,entradaColumnaIA

    elif(turno_IA == 1): ## SEGUNDO MOVIMIENTO IA

        if(board[1][1]!="O"):   ## SI NO HAY VALOR DEL USER EN EL MEDIO
            entradaFilaIA = random.randrange(0,3,2)
            entradaColumnaIA = random.randrange(0,3,2)    

            while (str(board[entradaFilaIA][entradaColumnaIA]).isdigit()==False):
                entradaFilaIA = random.randrange(0,3,2)
                entradaColumnaIA = random.randrange(0,3,2)
            
            return entradaFilaIA,entradaColumnaIA
            

        elif(board[1][1]=="O"): ## SI HAY VALOR DEL USER EN EL CENTRO

            if(fila_mvm_IA==0):
                entradaFilaIA=2
            else:
                entradaFilaIA=0
            if(col_mvm_IA==0):
                entradaColumnaIA=2
            else:
                entradaColumnaIA=0

            return entradaFilaIA,entradaColumnaIA

    win_condittion_var = win_condittion(board,combo_check)  ## FUNCION WIN CONDITIION A VARIABLE

    if(win_condittion_var[0]==True):    ## SI HAY WIN CONDITIION
        entradaFilaIA = win_condittion_var[1]
        entradaColumnaIA = win_condittion_var[2]
    
        return entradaFilaIA,entradaColumnaIA

    else:   ## SI NO HAY WIN CONDITIION
        entradaFilaIA = random.randrange(0,3,2)
        entradaColumnaIA = random.randrange(0,3,2)    

        while (str(board[entradaFilaIA][entradaColumnaIA]).isdigit()==False):
            entradaFilaIA = random.randrange(0,3,2)
            entradaColumnaIA = random.randrange(0,3,2)

        return entradaFilaIA,entradaColumnaIA

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
combo_check=[[""]]                                  ## CREA LA LISTAS DE LISTAS DE LOS COMBOS OCUPADOS
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
        combos_check(board,combo_check)         ## ACTUALIZA LOS COMBOS
        MakeListOfFreeFields(board)             ## LISTA DE POSICIONES VACIAS
        movement = EnterMove(board)             ## MOVIMIENTO USER
        board[movement[0]][movement[1]] = "O"   ## INSERTAR MOV USER

    elif game_mode_var == "2":
        combos_check(board,combo_check)                                             ## ACTUALIZA LOS COMBOS
        movement = DrawMove(board,turno_IA,movement[0],movement[1],combo_check)     ## MOVIMIENTO IA
        turno_IA += 1                                                               ## MAS 1 TURNO IA
        board[movement[0]][movement[1]] = "X"                                       ## INSERTAR MOV IA

    turnos += 1     ## TURNO +1

    if VictoryFor(board)=="X" or VictoryFor(board)=="O" or turnos == 9: ## MIRA SI HAY VICTORIA O NO HAY MAS TURNOS DISPONIBLES
        break
    
    if game_mode_var == "1" :
        combos_check(board,combo_check)                                             ## ACTUALIZA LOS COMBOS
        movement = DrawMove(board,turno_IA,movement[0],movement[1],combo_check)     ## MOVIMIENTO IA
        turno_IA += 1                                                               ## MAS 1 TURNO IA
        board[movement[0]][movement[1]] = "X"                                       ## INSERTAR MOV IA

    elif game_mode_var == "2":
        DisplayBoard(board)                     ## PRINTEA EL TABLERO
        combos_check(board,combo_check)         ## ACTUALIZA LOS COMBOS
        MakeListOfFreeFields(board)             ## LISTA DE POSICIONES VACIAS
        movement = EnterMove(board)             ## MOVIMIENTO USER
        board[movement[0]][movement[1]] = "O"   ## INSERTAR MOV USER

    turnos += 1     ## TURNO +1

    if VictoryFor(board)=="X" or VictoryFor(board)=="O" or (turnos == 9):   ## MIRA SI HAY VICTORIA O NO HAY MAS TURNOS DISPONIBLES
        break



if(VictoryFor(board)=="X"):
    print("\nEl ganador es la IA, (X)\nEl User ha perdido, (O)\n")
elif(VictoryFor(board)=="O"):
    print("\nEl ganador es User, (O)\nLa IA ha perdido, (X)\n")
elif turnos == 9:
    print("\nHa sido un empate tecnico\n")

DisplayBoard(board)









