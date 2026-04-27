#Crea un algoritmo donde el usuario ingresa una palabra y el sistema elimine las vocales 
#cosndiera que la palabra deve aser formateada a mayusculas
#cosnidera usar bucle for
#cosnidera que la nueva palabra formateada se imprima en una sola linea
print("---------------------------------------------------------------")
print("|------------ Bien venido al deverador de vocales ------------|")
print("---------------------------------------------------------------\n\n")

while True:
     
    word_user = input("Por favor ingrese una palabra o el numero cero '0' para salir: ").upper()
    word_format = ""

    if word_user == "0":
         break
    
    for i in range(len(word_user)):
            if word_user[i] == 'A' or word_user[i] == "E" or word_user[i] == "I" or word_user[i] == "O" or word_user[i] == "u":
                continue
            else:
                word_format += word_user[i]
            
    print(word_format)
print("\n\n---------------------------------------------------------------")
print("|--------- Gracias por jugar al devorador de vocales ---------|")
print("---------------------------------------------------------------")
