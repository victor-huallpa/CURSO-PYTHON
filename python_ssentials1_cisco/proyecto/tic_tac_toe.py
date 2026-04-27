"""
Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego;
no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
"""
from random import randrange

# Inicializar el tablero
board = [[3 * i + j + 1 for j in range(3)] for i in range(3)]
board[1][1] = 'X'  # La máquina empieza en el centro

def table(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def marcar_table(position, game):
    # Convertir posición 1-9 a coordenadas [fila][columna]
    pos = position - 1
    row = pos // 3
    col = pos % 3
    if board[row][col] not in ['X', 'O']:
        board[row][col] = game
        return True
    else:
        return False

def movi_bot():
    while True:
        position = randrange(1, 10)
        info = marcar_table(position, 'X')
        if info:
            print(f"\nEl bot marcó la posición {position}\n")
            break

def movi_user():
    while True:
        try:
            valor = int(input("Ingrese un valor disponible (1-9): "))
            if 1 <= valor <= 9:
                info = marcar_table(valor, 'O')
                if info:
                    break
                else:
                    print(f"La posición {valor} ya está ocupada. Intente de nuevo.")
            else:
                print("El número no está en el rango 1-9. Intente de nuevo.")
        except ValueError:
            print("El valor ingresado no es un número. Intente de nuevo.")

def ganador():
    # Revisar filas y columnas
    for i in range(3):
        # Filas
        if board[i][0] == board[i][1] == board[i][2]:
            return 'Bot' if board[i][0] == 'X' else 'Usuario'
        # Columnas
        if board[0][i] == board[1][i] == board[2][i]:
            return 'Bot' if board[0][i] == 'X' else 'Usuario'

    # Revisar diagonales
    if board[0][0] == board[1][1] == board[2][2]:
        return 'Bot' if board[0][0] == 'X' else 'Usuario'
    if board[0][2] == board[1][1] == board[2][0]:
        return 'Bot' if board[0][2] == 'X' else 'Usuario'

    return None

def tablero_lleno():
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True

# Juego principal
def juego():
    table(board)
    while True:
        movi_user()
        table(board)
        if ganador() == 'Usuario':
            print("¡Felicidades! Usted ganó.")
            break
        if tablero_lleno():
            print("Empate.")
            break
        movi_bot()
        table(board)
        if ganador() == 'Bot':
            print("El bot ganó.")
            break
        if tablero_lleno():
            print("Empate.")
            break

# Iniciar juego
juego()


