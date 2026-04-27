#existen 4 operadores de bit a bit, manipulan bit de datos individuales

#AND &
#OR |
#NOT ~
#XOR ^
a = 9  # Representación binaria: 0101
b = 3  # Representación binaria: 0011
resultado_and = a & b  # 0101 & 0011 = 0001 (1 en decimal)
resultado_or = a | b  # 0101 | 0011 = 0111 (7 en decimal)
resultado_not = ~a  # ~0101 = 1010 (10 en decimal)
resultado_xor = a ^ b  # 0101 ^ 0011 = 0110 (6 en decimal)

print(resultado_and)  # Salida: 1
print(resultado_or)  # Salida: 7
print(resultado_not)  # Salida: 10
print(resultado_xor)  # Salida: 6