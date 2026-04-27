#En las listas siempre se tiende a tener una gran cantidad de datos y en este caso, para llnarlas
#se usa una forma compresa de iteracion sobre las listas y llenarlas de informaicon

squares = [2**i for i in range(8)]#se eleva al exponente i ( 0-7) al numero 2
print(squares)

twos = [x **2 for x in range(10)]#a los numeros del 0 al 9 se eleva a la potencia 2
print(twos)

odds = [x for x in squares if x % 2 != 0]
print(odds)

#matriz arreglo bidimencional
board = []

EMPTY = 'CV'
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
for i in range(8):
    print(board[i])

print('\n')

board = [[EMPTY for i in range(8)] for j in range(8)]
board[0][0] = 'TB'
board[0][7] = 'TB'
board[7][0] = 'TN'
board[7][7] = 'TN'
board[4][2] = 'CN'
board[3][4] = 'PB'

for i in range(8):
    print(board[i])