var = 2
squares = [x ** var for x in range(10)]
print(squares)

odds = [x for x in squares if x % 2 != 0 ]

print(odds)

EMPTY=0
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
for i in range(len(board)):
    print(board[i], '\n\n\n')

board = [[i for i in range(8)] for j in range(8)]


    
ROOK = 'torre'
board[0][0] = ROOK
print(board[0][0] )
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
board[4][2] = 'KNIGHT'
board[3][4] = 'PAWN'


for i in range(len(board)):
    print(board[i])
    
temps = [[0.0 for h in range(24)] for d in range(31)]
for i in range(len(temps)):
    print(temps[i])



