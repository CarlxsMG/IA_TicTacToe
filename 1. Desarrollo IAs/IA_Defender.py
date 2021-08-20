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

## CHECKEA LAS LINEAS DE COMBO OCUPADAS DEL TABLERO -- RECORRE EL MAPA Y GUARDA EL COMBO OCUPADO -- EVITA FALLOS DE POSICION FICHA IA Y DE FALSAS VICTORIAS
def combos_check(board,combo_check):
    combo_true=False

    ## BUSQUEDA POR FILAS
    for i in range(3):
        count = 0
        combo = []

        for j in range(3):
            combo.append([i,j])     ## CREA EL COMBO

            if(board[i][j]=="X")or(board[i][j]=="O"):
                count +=1

        if(count==3):
            combo_true=False

            for i in range(len(combo_check)):
                if(combo_check[i] == combo):
                    combo_true = True
            
            if(combo_true == False):    ## SI EL COMBO, NO ESTA EN LA LISTA DE COMBOS OCUPADOS, SE AÑADE
                combo_check+=[combo]

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
            
            if(combo_true == False):    ## SI EL COMBO, NO ESTA EN LA LISTA DE COMBOS OCUPADOS, SE AÑADE
                combo_check+=[combo]

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

                    if(board[f_inv][q_inv])=="X" or (board[f_inv][q_inv])=="O":  ## COMPRUEBA QUE EN LAS ESQUINAS ENFRENTADAS TENGAN EL MISMO VALOR (X/O)
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

                    if(board[f_inv][q_inv])=="X" or (board[f_inv][q_inv])=="O":     ## COMPRUEBA QUE EN LAS ESQUINAS ENFRENTADAS TENGAN EL MISMO VALOR (X/O)
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

                if(board[i][n]!="O")and(board[i][n]!="X"):  ## BUSCA LA POSICION DISPONIBLE
                    ColumnaIA = n
                    win = True                              ## WIN CONDITTION DISPONIBLE
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
    if(board[1][1]=="O")or(board[1][1]=="X"):
        for f in range(0,3,2):
            for c in range(0,3,2):
                if(board[f][c]=="O")or(board[1][1]=="X"):   ## SI HAY VALOR CENTRAL
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
                        lista_variantes.append([win,FilaIA,ColumnaIA,board[f][c]])  ## INSERTA EL COMBO EN LAS JUGADAS DISPONIBLES EN ESE MOMENTO DEL TABLERO

    else:   ## SI NO HAY VALOR CENTRAL
        for b in range(0,3,2):
            if(board[0][b]=="X"):   ## BUSCA POR ESQUINAS PARA VALOR X
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

    if(len(lista_variantes)>1):     ## LA IA OBTIENE ELECCION DE RESPUESTA, CUANDO HAYA MAS DE 1 JUGADA DISPONIBLE
        for i in range(len(lista_variantes)):   ## RECORRE LAS JUGADAS DISPONIBLES

            if(lista_variantes[i][3]=="X"):     ## LAS JUGADAS DE LA IA OBTIENEN MAS IMPORTANCIA, QUE LOS CIERRES DEL CONTRINCARIO
                FilaIA=lista_variantes[i][1]
                ColumnaIA=lista_variantes[i][2]
            else:
                FilaIA=lista_variantes[1][1]
                ColumnaIA=lista_variantes[1][2]

    return win,FilaIA,ColumnaIA               

## MOVIMIENTO IA
def DrawMove(board):   
    import random

    win_condittion_var = win_condittion(board,combo_check)

    if(win_condittion_var[0] == True):
        entradaFilaIA = str(win_condittion_var[1])
        entradaColumnaIA = str(win_condittion_var[2])

    else:       
        entradaFilaIA = random.randrange(3)
        entradaColumnaIA = random.randrange(3)
        
        while int(entradaColumnaIA) != board[int(entradaFilaIA)][int(entradaColumnaIA)]:
            entradaFilaIA = random.randrange(3)
            entradaColumnaIA = random.randrange(3)
        
    board[int(entradaFilaIA)][int(entradaColumnaIA)] = "X"


## -------------------------------------------------------------------------------------------------------------------------

board = [[i for i in range(3)] for j in range(3)]
combo_check=[[""]]

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