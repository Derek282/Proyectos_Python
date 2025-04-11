from random import randrange
import time

def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for i in range(len(board)):
        for j in range(2,len(board),2):
            print("+-------+-------+-------+")
            print("|       |       |       |")
            print("|  ", board[i][j-2],"  |  ", board[i][j-1],"  |  ",board[i][j],"  |")
            print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    condicion = "tonto"
    while condicion == "tonto":
        respuesta = int(input("En que casilla quieres tirar? "))
        if respuesta <=0 or respuesta >= 10:
            print("No existe esa casilla")
            condicion = "tonto"
        elif respuesta > 0 and respuesta < 10:
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == respuesta:
                        board[i][j] = "O"
                        condicion = "si"
                        return condicion
                        #return display_board(board)
            print("la casilla esta siendo ocupada")
            condicion = "tonto"
    
def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    condicion = "no"
    while condicion == "no":
        move = randrange(10)
        print("la maquina elige: ",move)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == move:
                    board[i][j] = "X"
                    condicion = "si"
                    return condicion
                    #return display_board(board)
        print("la casilla ya esta ocupada va a elegir otra")
        condicion = "no"
    

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    global libres 
    libres = []
    for i in range(3):
        for j in range(3):
            casilla = board[i][j]
            if type(casilla) == int and 1 <= casilla <= 9:
                libres.append((i, j))
    return libres

def ganador(tabla, libres):
    global condicion
    ganador_encontrado = False  # Bandera para rastrear si encontramos un ganador
    for i in range(len(tabla)):
        for j in range(2, len(tabla[i])):
            if tabla[i][j-2] == "X" and tabla[i][j-1] == "X" and tabla[i][j] == "X":
                time.sleep(1)
                print("gana el X")
                print("gana en filas")
                condicion = "ganadorX"
                ganador_encontrado = True
                return condicion

            if tabla[i][j-2] == "O" and tabla[i][j-1] == "O" and tabla[i][j] == "O":
                time.sleep(1)
                print("gana el O")
                print("gana en filas")
                condicion = "ganador"
                ganador_encontrado = True
                return condicion
                
    
    if not ganador_encontrado:
        for i in range(len(tabla)):
            for j in range(2, len(tabla[i])):
                if tabla[j-2][i] == "X" and tabla[j-1][i] == "X" and tabla[j][i] == "X":
                    time.sleep(1)
                    print("gana el X")
                    print("gana en columnas")
                    condicion = "ganadorX"
                    ganador_encontrado = True
                    return condicion

                if tabla[j-2][i] == "O" and tabla[j-1][i] == "O" and tabla[j][i] == "O":
                    time.sleep(1)
                    print("gana el O")
                    print("gana en columnas")
                    condicion = "ganador"
                    ganador_encontrado = True
                    return condicion

            
    if not ganador_encontrado:
        if tabla[0][0] == "X" and tabla[1][1] == "X" and tabla[2][2] == "X":
            time.sleep(1)
            print("gana el X")
            print("gana en diagonal izquierda")
            condicion = "ganadorX"
            ganador_encontrado = True
            return condicion
        
        if tabla[0][0] == "O" and tabla[1][1] == "O" and tabla[2][2] == "O":
            time.sleep(1)
            print("gana el O")
            print("gana en diagonal izquierda")
            condicion = "ganador"
            ganador_encontrado = True
            return condicion

            
    if not ganador_encontrado:
        if tabla[0][2] == "X" and tabla[1][1] == "X" and tabla[2][0] == "X":
            time.sleep(1)
            print("gana el X")
            print("gana en diagonal derecha")
            condicion = "ganadorX"
            ganador_encontrado = True
            return condicion
        
        if tabla[0][2] == "O" and tabla[1][1] == "O" and tabla[2][0] == "O":
            time.sleep(1)
            print("gana el O")
            print("gana en diagonal derecha")
            condicion = "ganador"
            ganador_encontrado = True
            return condicion

    if not ganador_encontrado:
        if libres == []:
            time.sleep(1)
            print("Es un empate")
            condicion = "empate"
            return condicion 
        else:
            condicion = "no"
            return condicion

#main
ele1 = [1,2,3]
ele2 = [4,"X",6]
ele3 = [7,8,9]
tablero = [ele1,ele2,ele3]
condicion = "no"

while condicion == "no":
    display_board(tablero)
    if condicion == "no":
        enter_move(tablero)
        make_list_of_free_fields(tablero)
        ganador(tablero,libres)
    
    if condicion == "no":
        display_board(tablero)
        time.sleep(1)
        draw_move(tablero)
        time.sleep(1)
        make_list_of_free_fields(tablero)
        ganador(tablero,libres)
display_board(tablero)