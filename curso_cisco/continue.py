# # Indicar al usuario que ingrese una palabra
# print('_______________________________')
# print('|juego del devorador de palabra|')
# print('_______________________________\n')
# user_word = str(input('ingrese una plabra por favor: ')).upper()
# # y asignarlo a la variable user_word.

# for letter in user_word:
#     if letter in "AEIOU":
#         continue
    
#     print(letter)
#Completa el cuerpo del bucle for.
blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	

altura= 1
i=1
for i in blocks:
    blocks -= i
    altura += 1
    blocks += 1
print("La altura de la pirámide:", altura)
    
